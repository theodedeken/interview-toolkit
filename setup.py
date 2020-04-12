# SPDX-FileCopyrightText: 2020 Theo Dedeken
#
# SPDX-License-Identifier: MIT

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='interview-toolkit',
      version='0.1',
      description='Scripts to generate cv and cover letter',
      url='https://github.com/theodedeken/interview-toolkit',
      author='Theo Dedeken',
      author_email='theo.dedeken@telenet.be',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=['interview_toolkit'],
      scripts=['scripts/interview-toolkit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "yaml",
      ],)
