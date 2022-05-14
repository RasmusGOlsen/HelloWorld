from setuptools import setup, find_packages

setup(
    name='app',
    description='My application',
    author='Rasmus Olsen',
    author_email='rasmus.g.olsen@gmail.com',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['hello=src.helloworld:main'],
    }
)
