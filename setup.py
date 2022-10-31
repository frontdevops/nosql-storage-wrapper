#!/usr/bin/env python3
import sys
import pathlib
import tomli
from setuptools import find_packages, setup

WORK_DIR = pathlib.Path(__file__).parent

# Check python version
MINIMAL_PY_VERSION = (3, 10, 8)
if sys.version_info < MINIMAL_PY_VERSION:
    raise RuntimeError("aiogram works only with Python {}+".format(".".join(map(str, MINIMAL_PY_VERSION))))


def get_description() -> str:
    """
    Read full description from "README.rst"
    :return: description
    :rtype: str
    """
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


def parse_project_toml() -> dict:
    """
    Read version
    :return: str
    """
    try:
        with open("pyproject.toml", "rb") as f:
            return tomli.load(f)
    except IndexError:
        raise RuntimeError("Unable to determine version.")


project_meta = parse_project_toml()


setup(
    name=project_meta["project"]["name"],
    version=project_meta["project"]["version"],
    license="MIT",
    author=project_meta["project"]["authors"][0]["name"],
    author_email=project_meta["project"]["authors"][0]["email"],
    description=project_meta["project"]["description"],
    long_description=get_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/frontdevops/nosql-storage-wrapper",
    download_url="https://github.com/frontdevops/nosql-storage-wrapper/archive/refs/tags/0.1.9.tar.gz",
    project_urls={
        "Documentation": "https://github.com/frontdevops/nosql-storage-wrapper/blob/main/README.md",
        "Source": "https://github.com/frontdevops/nosql-storage-wrapper",
        "Bug Tracker": "https://github.com/frontdevops/nosql-storage-wrapper/issues",
    },
    keywords=["pypi", "config", "tutorial"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10.8",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Application Utilities",
    ],
    package_dir={"": "magic_config"},
    packages=find_packages(where=project_meta["project"]["name"],
                           exclude=("tests", "tests.*", "examples.*", "docs",)
                           ),
    include_package_data=False,
    python_requires=">=3.10.8",
    install_requires=[
        "motor==3.1.1",
        "pymongo==4.3.2",
        "magic_config==0.1.10",
    ],
    extras_require={
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine"
        ]
    },
)
