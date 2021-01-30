# %% Get all markdown files in the repo

import git

NOTES_REPO_DIR = "../"
TAGS_DIR = "../Tags/"
TAG_SEPARATOR = ","

repo = git.Git(NOTES_REPO_DIR)

md_files = [
    file_.strip()
    for file_ in
    repo.ls_files().split("\n")
    if file_.strip().endswith(".md")
]

# %% Find all tags in each file

import re
import collections

TAGS_RE = re.compile(r'^tags: *\[?([^\]]+)\]? *$', re.M)

tags_to_docs = collections.defaultdict(list)

for md_file_name in md_files:
    with open(NOTES_REPO_DIR + md_file_name) as md_file:
        contents = md_file.read()
        re_match = TAGS_RE.search(contents)

        if not re_match: continue

        tags = (
            tag.strip('" ')
            for tag in
            re_match.group(1).split(TAG_SEPARATOR)
        )

        for tag in tags:
            tags_to_docs[tag].append(md_file_name)

# %% Generate a directory of files that relate tags to filenames

import os
import shutil

shutil.rmtree(TAGS_DIR)
os.makedirs(TAGS_DIR, exist_ok=True)

for tag, filenames in tags_to_docs.items():
    with open(TAGS_DIR + tag + ".md", "w") as tag_file:
        tag_file.write(f"---{os.linesep}")
        tag_file.write(f"type: tagged_files{os.linesep}")
        tag_file.write(f"---{os.linesep}")

        tag_file.write(f'# Tagged: "{tag}"')

        tag_file.write(os.linesep)
        tag_file.write(os.linesep)

        tag_file.writelines((
            f"- [[../{filename}]]{os.linesep}"
            for filename in
            filenames
        ))

# %%
