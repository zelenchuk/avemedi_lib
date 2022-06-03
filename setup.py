# https://docs.pytest.org/en/6.2.x/goodpractices.html

from setuptools import find_packages, setup

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='avemedi_lib',
    packages=find_packages(include=['avemedi_lib']),
    version='0.1.6',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='This library help in getting a "average value of numbers list" and "get median (for ordered, unordered list of numbers and even or odd list values)". Enjoy.',
    author='zelenchyks@gmail.com',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.2'],
    test_suite='tests',
    python_requires=">=3.6"
)
