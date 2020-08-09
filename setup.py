"""setup.py"""

import os
import re

import setuptools


def get_long_description():
    """Get long description"""
    base_dir = os.path.abspath(os.path.dirname(__file__))
    readme_file = os.path.join(base_dir, "README.md")
    with open(readme_file, "r") as opened_file:
        return opened_file.read()


def get_current_version():
    """Get current version"""
    base_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(base_dir, "evaluations", "__init__.py")
    with open(version_file, 'r') as opened_file:
        return re.search(
            r'^__version__ = [\'"]([^\'"]*)[\'"]', opened_file.read(), re.M
        ).group(1)


setuptools.setup(
    name="evaluations",
    version=get_current_version(),
    author="Yaroslav Isaienkov",
    author_email="oiuygl@gmail.com",
    description="The library for models evaluation",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/yisaienkov/evaluations",
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={"tests": ["pytest"]},
)
