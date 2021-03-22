# CoV Mutation

This is a tool for converting nucleotide and amino acid mutations for SARS-CoV-2 such as those found on https://covariants.org/variants/S.N501

## Installing

Clone the repository and run

`pip install .`

This will install the Python library and the CLI.

## Usage example

```
$ cov_mutation nt A23063T
A23063T causes S:N501Y
$ cov_mutation aa S:E484K
G23012A causes S:E484K
```
