#!/usr/bin/env python
"""
Setup package.
"""
import os
import re
from setuptools import setup


def get_version(filename):
    """One of the practical options for single source of versioning. See:
    https://packaging.python.org/guides/single-sourcing-package-version/

    filename arg is relative to this file"""

    version_file_name = os.path.join(os.path.dirname(__file__), filename)
    with open(version_file_name, "r") as version_file:
        find_version = re.compile(r"^__version__ = [\'\"]([^\'\"]*)[\'\"]")
        for line in version_file.readlines():
            match = find_version.search(line)
            if match:
                return match.group(1)

    raise RuntimeError("Error, unable to locate version string")


setup(
    name="riptr",
    version=get_version("riptr.py"),
    description="Replacement for tr/sed replace in python",
    author="Noah Pendleton",
    author_email="2538614+noahp@users.noreply.github.com",
    url="https://github.com/noahp/python-riptr",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # using markdown as pypi description:
    # https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi
    setup_requires=["setuptools>=38.6.0", "wheel>=0.31.0", "twine>=1.11.0"],
    # doesn't export anything useful right now.
    py_modules=["riptr"],
    entry_points={"console_scripts": ["riptr = riptr:main", "rtr = riptr:main"]},
    # correct shebang replacement, from https://github.com/pybuilder/pybuilder/issues/168
    options={"build_scripts": {"executable": "/usr/bin/env python"}},
)
