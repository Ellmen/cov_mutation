from .cmds import aa, nt


class CovMutation(object):
    """Translate between nucleotide and amino acid mutations for SARS-CoV-2"""

    def __str__(self):
        return "Translate between nucleotide and amino acid mutations for SARS-CoV-2"

    def aa(self, mut):
        aa(mut)

    def nt(self, mut):
        nt(mut)
