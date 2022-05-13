import setuptools
from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(_here, 'clinsent', 'version.py')) as f:
    exec(f.read(), version)
    
with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'clinsent',
    url = 'https://github.com/ck37/clinsent',
    author = 'Chris Kennedy, Hunter Mills, Julien Cobert',
    author_email = 'chrisken@gmail.com',
    packages = setuptools.find_packages(),
    install_requires = ['importlib_resources', 'pandas', 'spacy', 'cython', 'quicksect', 'medspacy', 'pysbd'],
    version = version['__version__'],
    long_description_content_type = "text/markdown",
    license = 'MIT',
    description = 'Tools to measure sentiment in clinical notes',
    long_description = long_description,
    python_requires = '>=3.6',
)
