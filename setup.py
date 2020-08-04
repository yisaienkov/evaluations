"""setup.py"""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="evaluations",
    version="0.0.1",
    author="Yaroslav Isaienkov",
    author_email="oiuygl@gmail.com",
    description="The library for models evaluation",
    long_description=LONG_DESCRIPTION,
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
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
