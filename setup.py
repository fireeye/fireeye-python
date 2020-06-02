# Copyright (C) 2019 FireEye, Inc. All Rights Reserved.
from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="fireeyepy",
  version="1.0.0",
  description="FireEye Client Library for Python",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/fireeye/fireeye-python",
  author="FireEye",
  author_email="developers@fireeye.com",
  license="MIT",
  packages=["fireeyepy"],
  platforms=["any"],
  install_requires=["requests>=2.4.2"],
  python_requires='>=3.6',
)