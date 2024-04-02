#!/usr/bin/env python

import os
import subprocess
import json

MAIN_BRANCH_NAME = "main"
STATS_FILE = "./.stats/stats.json"
STATS_VERSION = 1

def compute_stats(commit_hash: str) -> dict:
    stats = {}

    result = subprocess.run(f"git log -1 --format='%aI' {commit_hash}".split(), stdout=subprocess.PIPE)
    result.check_returncode()
    stats['timestamp'] = str(result.stdout, 'utf-8').strip("'\" \r\n")

    result = subprocess.run(f"git ls-tree -r {commit_hash}".split(), stdout=subprocess.PIPE)
    result.check_returncode()
    file_list = str(result.stdout, 'utf-8').splitlines()

    stats["num_files"] = len(file_list)

    num_words = 0
    markdown_files = [ f.split('\t')[-1] for f in file_list if f.endswith('.md') ]
    for md_file in markdown_files:
        result = subprocess.run(["git", "show", f"{commit_hash}:{md_file}"], stdout=subprocess.PIPE)
        result.check_returncode()
        contents = result.stdout
        num_words += len(contents.split())

    stats['num_words'] = num_words

    stats["version"] = STATS_VERSION

    return stats

def main():
    try:
        with open(STATS_FILE, 'r') as f:
            stats: dict[str, dict] = json.load(f)
    except FileNotFoundError:
        stats = {}

    # Check for changes
    # result = subprocess.run("git diff-index --quiet HEAD --".split())
    # result.check_returncode()

    # Get the list of commit hashes
    result = subprocess.run(f'git log --format="%H" {MAIN_BRANCH_NAME}'.split(), stdout=subprocess.PIPE)
    result.check_returncode()

    try:
        commit_hashes = str(result.stdout, 'utf-8').replace('"', '').splitlines()
        for i, hash in enumerate(commit_hashes):
            print(f"Getting stats for commit {hash}. {i+1} of {len(commit_hashes)}")
            if hash not in stats or stats[hash].get('version', 0) < STATS_VERSION:
                stats[hash] = compute_stats(hash)
    finally:
        with open(STATS_FILE, 'w') as f:
            json.dump(stats, f, indent=2)

if __name__ == "__main__":
    main()
