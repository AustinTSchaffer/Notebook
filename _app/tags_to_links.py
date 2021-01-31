# %% Get all markdown files in the repo

import os
import shutil

NOTES_DIR = "../"
TAGS_DIR = "../Tags/"
TAG_SEPARATOR = ","
CREATE_UNTAGGED = True
UNTAGGED_TAG_NAME = "Untagged"

shutil.rmtree(TAGS_DIR, ignore_errors=True)
os.makedirs(TAGS_DIR, exist_ok=True)

def rec_find_files(dir):
    for path in os.listdir(dir):
        path = os.path.join(dir, path)
        if os.path.isdir(path):
            yield from rec_find_files(path)
        else:
            yield path

md_files = [
    file_relpath
    for file_relpath in
    rec_find_files(NOTES_DIR)
    if file_relpath.endswith(".md")
]

# %% Find all tags in each file

import re
import collections

TAGS_RE = re.compile(r'^tags: *\[?([^\]\n]+)\]? *$', re.M)

tags_to_docs = collections.defaultdict(list)

for md_file_name in md_files:
    with open(md_file_name) as md_file:
        contents = md_file.read()

    re_match = TAGS_RE.search(contents)

    if not re_match:
        if CREATE_UNTAGGED:
            tags_to_docs[UNTAGGED_TAG_NAME].append(md_file_name)
        continue

    tags = (
        tag.strip('" ')
        for tag in
        re_match.group(1).split(TAG_SEPARATOR)
    )

    for tag in tags:
        tags_to_docs[tag].append(md_file_name)

# %% Generate a directory of files that relate tags to filenames

for tag, filenames in tags_to_docs.items():
    output_file_name = os.path.join(TAGS_DIR, f"{tag}.md")
    with open(output_file_name, "w") as tag_file:
        tag_file.write(f"---{os.linesep}")
        tag_file.write(f"type: tag{os.linesep}")
        tag_file.write(f"---{os.linesep}")

        tag_file.write(f'# {tag}')

        tag_file.write(os.linesep)
        tag_file.write(os.linesep)

        tag_file.writelines((
            f"- [[{os.path.relpath(filename, TAGS_DIR)}]]{os.linesep}"
            for filename in
            filenames
        ))

# %%
