# Copyright (C) 2019 FireEye, Inc. All Rights Reserved.
from setuptools import setup

setup(
  name="fireeyepy",
  version="0.0.2",
  description="FireEye Client Library for Python",
  url="https://github.com/fireeye/fireeye-python",
  author="FireEye",
  license="MIT",
  packages=["detection_on_demand/detection"],
  platforms=["any"],
  install_requires=["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
)