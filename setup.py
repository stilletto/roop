from setuptools import setup

with open('requirements-headless.txt') as f:
    required = f.read().splitlines()
setup(
    name='roop',
    version='0.1.0',
    packages=['roop', 'roop.processors', 'roop.processors.frame'],
    url='',
    license='',
    author='A',
    author_email='',
    description='',
    install_requires=required,
)
