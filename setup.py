# Copyright (C) 2019 FireEye, Inc. All Rights Reserved.
from setuptools import setup

setup(
  name="fireeyepy",
  version="0.1.0",
  description="FireEye Client Library for Python",
  url="https://github.com/fireeye/fireeye-python",
  author="FireEye",
  license="MIT",
  packages=["fireeyepy"],
  platforms=["any"],
  install_requires=["requests>=2.4.2"]
)