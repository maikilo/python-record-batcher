from setuptools import find_packages, setup

setup(
    name='batches',
    packages=find_packages(include=['batches']),
    version='0.1.0',
    description='A simple python library for batching records.',
    author='maikilo',
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    test_suite='tests',
)
