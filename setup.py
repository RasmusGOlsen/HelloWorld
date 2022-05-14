from setuptools import setup, find_packages
from src.helloworld import __version__, __author__, __email__


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='HelloWorld',
    description='A Hello World application to showcase a Python package',
    long_description=long_description,
    url='https://github.com/RasmusGOlsen/HelloWorld',
    author=__author__,
    author_email=__email__,
    version=__version__,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': ['hello=helloworld.helloworld:main'],
    },
    install_requires=[],
    extras_require={
        'dev': ['tox', 'pytest', 'flake8'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    project_urls={
        'Source': 'https://github.com/RasmusGOlsen/HelloWorld',
        'Tracker': 'https://github.com/RasmusGOlsen/HelloWorld/issues',
    },
)
