"""Setup of ProjectEuler package."""

from setuptools import setup

setup(
    name='TowelStuff',
    version='0.1.0',
    author='Henry Heath',
    author_email='henryjheath@gmail.com',
    packages=['projecteuler', 'projecteuler.test'],
    package_dir={'projecteuler': '/projecteuler'},
    package_data={'projecteuler': ['data/*.dat']},
    scripts=[],
    url='https://github.com/heathy/ProjectEuler',
    license='LICENSE.txt',
    description='Package to solve Project Euler problems',
    long_description=open('README.md').read(),
    install_requires=[],
)
