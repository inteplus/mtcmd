#!/usr/bin/env python3

import os
from setuptools import setup, find_namespace_packages

VERSION_FILE = os.path.join(os.path.dirname(__file__), "VERSION.txt")

setup(
    name="mtcmd",
    description="Minh-Tri Pham's common Linux scripts",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=["mt.*"]),
    scripts=[
        "scripts/git_binst.sh",
        "scripts/git_emac.sh",
        "scripts/git_commit_sync.sh",
        "scripts/mt_update.py",
    ],
    install_requires=[
        "mtbase",
    ],
    url="https://github.com/inteplus/mtcmd",
    project_urls={
        "Documentation": "https://mtdoc.readthedocs.io/en/latest/mt.cmd/mt.cmd.html",
        "Source Code": "https://github.com/inteplus/mtcmd",
    },
    setup_requires=["setuptools-git-versioning<2"],
    setuptools_git_versioning={
        "enabled": True,
        "version_file": VERSION_FILE,
        "count_commits_from_version_file": True,
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}+{branch}",
        "dirty_template": "{tag}.post{ccount}",
    },
)
