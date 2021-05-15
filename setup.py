#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mercy_reader',
    version='0.0.1-1',
    author='Daniel Han',
    author_email='hex0cter@gmail.com',
    maintainer='Daniel Han',
    maintainer_email='hex0cter@gmail.com',
    license='MIT',
    url='https://github.com/hex0cter/mercy-reader',
    description=(
        'Convert web page into other formats.'
        ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=['mercy_reader']),
    package_data={},
    python_requires='>=3.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
      'certifi==2018.11.29',
      'chardet==3.0.4',
      'html2text==2018.1.9',
      'idna==2.8',
      'Naked==0.1.31',
      'PyYAML==5.4',
      'requests==2.25.1',
      'urllib3==1.26.4',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
