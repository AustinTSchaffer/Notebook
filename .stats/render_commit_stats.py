import subprocess
import json
import re
import os
import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MAIN_BRANCH_NAME = "main"
STATS_FILE = "./.stats/data/stats.json"
STATS_VERSION = 2
WORD_RE = re.compile(rb"(\w*-\w+)|(\w+-\w*)|(\w*'\w+)|(\w+'\w*)|(\w+)")
NOTES_DIRECTORY = os.environ.get("NOTES_DIRECTORY", None)


def compute_stats(commit_hash: str) -> dict:
    stats = {}

    result = subprocess.run(
        f"git log -1 --format='%aI' {commit_hash}".split(), stdout=subprocess.PIPE
    )

    result.check_returncode()
    stats["timestamp"] = str(result.stdout, "utf-8").strip("'\" \r\n")

    result = subprocess.run(
        f"git ls-tree -r {commit_hash}".split(), stdout=subprocess.PIPE
    )

    result.check_returncode()
    file_list = str(result.stdout, "utf-8").splitlines()

    stats["num_files"] = len(file_list)

    num_words = 0
    markdown_files = [f.split("\t")[-1] for f in file_list if f.endswith(".md")]

    markdown_files = [
        f
        for f in markdown_files
        if not NOTES_DIRECTORY or f.startswith(NOTES_DIRECTORY)
    ]

    stats["num_md_files"] = len(markdown_files)

    for md_file in markdown_files:
        result = subprocess.run(
            ["git", "show", f"{commit_hash}:{md_file}"], stdout=subprocess.PIPE
        )

        result.check_returncode()
        for _ in WORD_RE.finditer(result.stdout):
            num_words += 1

    stats["num_words"] = num_words

    stats["version"] = STATS_VERSION

    return stats


def generate_commit_stats():
    try:
        with open(STATS_FILE, "r") as f:
            stats: dict[str, dict] = json.load(f)
    except FileNotFoundError:
        stats = {}

    # Check for changes
    # result = subprocess.run("git diff-index --quiet HEAD --".split())
    # result.check_returncode()

    # Get the list of commit hashes
    result = subprocess.run(
        f'git log --format="%H" {MAIN_BRANCH_NAME}'.split(), stdout=subprocess.PIPE
    )
    result.check_returncode()

    try:
        commit_hashes = str(result.stdout, "utf-8").replace('"', "").splitlines()
        for i, hash in enumerate(commit_hashes):
            print(f"Getting stats for commit {hash}. {i + 1} of {len(commit_hashes)}")
            if hash not in stats or stats[hash].get("version", 0) < STATS_VERSION:
                stats[hash] = compute_stats(hash)
    finally:
        with open(STATS_FILE, "w") as f:
            json.dump(stats, f, indent=2)


def render_commit_stats():
    df_stats = pd.read_json("./.stats/data/stats.json")
    df_stats = df_stats.T
    df_stats.timestamp = pd.Series.apply(
        df_stats.timestamp, datetime.datetime.fromisoformat
    )

    # The commits from merging in the "Foam" notebook base breaks
    # the graph a litte bit.
    df_stats = df_stats[df_stats.num_words > 5500]
    df_stats = df_stats.sort_values("timestamp")

    sns.set_theme()

    sns.lineplot(x=df_stats.timestamp, y=df_stats.num_words)
    plt.title("Word Count over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Word Count")

    plt.yticks(
        ticks=[n for n in range(50_000, 301_000, 50_000)],
        labels=[f"{n}k" for n in range(50, 301, 50)],
    )

    plt.savefig("./images/rendered/wordcount.png")

    plt.clf()

    sns.lineplot(x=df_stats.timestamp, y=df_stats.num_files)
    plt.title("File Count over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("File Count")
    plt.savefig("./images/rendered/filecount.png")


if __name__ == "__main__":
    generate_commit_stats()
    render_commit_stats()
