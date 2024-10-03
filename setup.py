from setuptools import setup, find_packages

setup(
    name='pycicd',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pycicd=src.cli:main',
        ],
    },
)