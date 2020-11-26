#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages
from mt.cmd.version import version

setup(name='mtcmd',
      version=version,
      description="Minh-Tri Pham's common Linux scripts",
      author=["Minh-Tri Pham"],
      packages=find_namespace_packages(include=['mt.*']),
      scripts=[
          'scripts/git_binst.sh',
          'scripts/git_cd.sh',
      ],
      install_requires=[
          'mtbase',
      ],
      url='https://github.com/inteplus/mtcmd',
      project_urls={
          'Documentation': 'https://mtdoc.readthedocs.io/en/latest/mt.cmd/mt.cmd.html',
          'Source Code': 'https://github.com/inteplus/mtcmd',
          }
      )
