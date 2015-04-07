"""Setup of ProjectEuler package."""

from distutils.core import setup

setup(
    name='TowelStuff',
    version='0.1.0',
    author='Henry Heath',
    author_email='henryjheath@gmail.com',
    packages=['projecteuler', 'projecteuler.test'],
    scripts=[],
    url='https://github.com/heathy/ProjectEuler',
    license='LICENSE.txt',
    description='Package to solve Project Euler problems',
    long_description=open('README.txt').read(),
    install_requires=[],
)
