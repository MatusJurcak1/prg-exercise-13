import matplotlib.pyplot as plt

class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence.upper()   # vždy uložíme velkými písmeny

    def length(self):
        return len(self.sequence)

    def __str__(self):
        return f"[{self.name}] délka={self.length()} nt, začátek: {self.sequence[:8]}..."


class DNASequence(Sequence):
    def gc_content(self):
        cg_count = 0
        dlzka_seq = len(self.sequence)
        for n in self.sequence:
            if n == "C" or n == "G":
                cg_count += 1
        return cg_count / dlzka_seq

    def base_counts(self):
        slovnik_baz = {"A": 0, "C": 0, "G": 0, "T": 0}
        for n in self.sequence:
            if n == "A":
                slovnik_baz["A"] += 1
            elif n == "C":
                slovnik_baz["C"] += 1
            elif n == "G":
                slovnik_baz["G"] += 1
            elif n == "T":
                slovnik_baz["T"] += 1
        return slovnik_baz

    def plot_composition(self):
        counts = self.base_counts()
        bases = ["A", "C", "G", "T"]
        values = [counts[b] for b in bases]
        colors = ["tab:green", "tab:blue", "tab:orange", "tab:red"]

        plt.figure(figsize=(5, 3))
        plt.bar(bases, values, color=colors, edgecolor="black")
        plt.title(f"Složení bází: {self.name}")
        plt.ylabel("Počet")
        plt.tight_layout()
        plt.show()

    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "T"}

    def to_rna(self):
        return RNASequence(self.name, self.sequence.replace("T", "U"))

class RNASequence(Sequence):
    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "U"}

    def codons(self):
        return [self.sequence[i:i + 3] for i in range(0, len(self.sequence) - 2, 3)]

    def find_start_codon(self):
        idx = self.sequence.find("AUG")
        if idx:
            return idx
        else:
            return -1


seq = Sequence("testovací", "acgtagctagc")
dna = DNASequence("mini", "ACCGGGTT")
dna2 = DNASequence("tuberculosis", "TTGACCGATGACCCCGGTTCAGGCTTCACCACAGTGTGGAACGCGGTCGTCTCCGAACTTAACGGCGACCCTAAGGTTGACGACGGACCCAGCAGTGATGCTAATCTCAGCGCTCCGCTGACCCCTCAGCAAAGGGCTTGGCTCAATCTCGTCCAGCCATTGACCATCGTCGAGGGGTTTGCTCTGTTATCCGTGCCGAGCAGCTTTGTCCAAAACGAAATCGAGCGCCATCTGCGGGCCCCGATTACCGACGCTCTCAGCCGCCGACTCGGACATCAGATCCAACTCGGGGTCCGCATCGCTCCGCCGGCGACCGACGAAGCCGACGACACTACCGTGCCGCCTTCCGAAAATCCTGCTACCACATCGCCAGACACCACAACCGACAACGACGAGATTGATGACAGCGCTGCGGCACGGGGCGATAACCAGCACAGTTGGCCAAGTTACTTCACCGAGCGCCCGCACAATACCGATTCCGCTACCGCTGGCGTAACCAGCCTTAACCGTCGCTACACCTTTGATACGTTCGTTATCGGCGCCTCCAACCGGTTCGCGCACGCCGCCGCCTTGGCGATCGCAGAAGCACCCGCCCGCGCTTACAACCCCCTGTTCATCTGGGGCGAGTCCGGTCTCGGCAAGACACACCTGCTACACGCGGCAGGCAACTATGCCCAACGGTTGTTCCCGGGAATGCGGGTCAAATATGTCTCCACCGAGGAATTCACCAACGACTTCATTAACTCGCTCCGCGATGACCGCAAGGTCGCATTCAAACGCAGCTACCGCGACGTAGACGTGCTGTTGGTCGACGACATCCAATTCATTGAAGGCAAAGAGGGTATTCAAGAGGAGTTCTTCCACACCTTCAACACCTTGCACAATGCCAACAAGCAAATCGTCATCTCATCTGACCGCCCACCCAAGCAGCTCGCCACCCTCGAGGACCGGCTGAGAACCCGCTTTGAGTGGGGGCTGATCACTGACGTACAACCACCCGAGCTGGAGACCCGCATCGCCATCTTGCGCAAGAAAGCACAGATGGAACGGCTCGCGGTCCCCGACGATGTCCTCGAACTCATCGCCAGCAGTATCGAACGCAATATCCGTGAACTCGAGGGCGCGCTGATCCGGGTCACCGCGTTCGCCTCATTGAACAAAACACCAATCGACAAAGCGCTGGCCGAGATTGTGCTTCGCGATCTGATCGCCGACGCCAACACCATGCAAATCAGCGCGGCGACGATCATGGCTGCCACCGCCGAATACTTCGACACTACCGTCGAAGAGCTTCGCGGGCCCGGCAAGACCCGAGCACTGGCCCAGTCACGACAGATTGCGATGTACCTGTGTCGTGAGCTCACCGATCTTTCGTTGCCCAAAATCGGCCAAGCGTTCGGCCGTGATCACACAACCGTCATGTACGCCCAACGCAAGATCCTGTCCGAGATGGCCGAGCGCCGTGAGGTCTTTGATCACGTCAAAGAACTCACCACTCGCATCCGTCAGCGCTCCAAGCGCTAG")
dna3 = DNASequence("priklad2", "ATCGCGGCTAATTCCGAT")
dna4 = DNASequence("priklad3", "ATCGCAATTCCATTTTATATATAT")
dna5 = DNASequence("platná",   "ACGCTAGCTAGC")
dna6 = DNASequence("neplatná", "ACGCNTAGCTAGC")   # N = neznámá báze

print(seq)            # [testovací] délka=11 nt, začátek: ACGTAGCT...
print(seq.length())   # 11
print(seq.sequence)   # ACGTAGCTAGC – automaticky převedeno na velká písmena
print(dna.base_counts())   # {"A": 1, "C": 2, "G": 3, "T": 2}
print(dna2.length())
print(dna2.gc_content())
print(dna3.gc_content())
print(dna3.base_counts())
print(dna4.gc_content())
print(dna4.base_counts())
dna2.plot_composition()
dna4.plot_composition()
print(dna5.is_valid())   # True
print(dna6.is_valid())   # False
print(RNASequence("správná",   "ACGUACGU").is_valid())   # True
print(RNASequence("s thyminem","ACGTACGU").is_valid())   # False — T v RNA být nemá
rna = RNASequence("mini", "AUGGCUUAA")
print(rna.codons())   # ["AUG", "GCU", "UAA"]
rna2 = RNASequence("zbytek", "AUGGCUUA")
print(rna2.codons())  # ["AUG", "GCU"]   — poslední dvě písmena netvoří celý kodon
rna = RNASequence("gen", "CCAUGGCUUAA")
print(rna.find_start_codon())   # 2   — AUG začíná na indexu 2
dna = DNASequence("gen_01", "CCATGGCTTAA")

rna = dna.to_rna()
print(rna)                          # __str__ zděděné ze Sequence
print(rna.is_valid())               # True
print(rna.find_start_codon())       # pozice prvního AUG
print(rna.codons())                 # seznam kodonů
