from setuptools import setup, find_packages
import os

def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()

setup(
    name='imputex',
    packages=find_packages(exclude=('tests', 'examples')),
    version='0.0.1',
    license='MIT',
    description='',
    long_description='',
    author='Manraj Singh',
    author_email='manrajsinghgrover@gmail.com',
    url='',
    keywords=[],
    install_requires=dependencies('requirements.txt'),
    tests_require=dependencies('requirements-dev.txt'),
    include_package_data=True
)
