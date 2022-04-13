#!/usr/bin/python

from setuptools import setup

setup(
    name="filetopq",
    version="0.0.1",
    description="convert files to parquet",
    author="Leo Liu",
    author_email="leo.liu@unsw.edu.au",
    scripts=["filetopq/filetopq"],
    packages=[
        "filetopq",
    ],
    install_requires=[
        "pandas",
        "pyarrow",
        "pyreadstat",
        "loguru",
    ],
)
