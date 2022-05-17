from setuptools import setup, find_packages
from src import __version__, __author__, __email__

setup(
    name='app',
    description='My application',
    author=__author__,
    author_email=__email__,
    version=__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['hello=src.helloworld:main'],
    }
)
