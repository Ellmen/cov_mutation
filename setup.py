from setuptools import setup

setup(
    name='cov_mutation',
    version='0.1',
    description='Translate between nucleotide and amino acid mutations for SARS-CoV-2',
    author='Isaac Ellmen',
    author_email='isaac.ellmen@uwaterloo.ca',
    packages=['cov_mutation'],
    install_requires=[
        'fire',
    ],
    entry_points={
        'console_scripts': ['cov_mutation=cov_mutation.command_line:main'],
    }
)
