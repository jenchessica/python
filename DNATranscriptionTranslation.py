def MakeProtein(DNATemplatedStrand):
    mRNA=""
    for nucleotide in DNATemplatedStrand:
            if nucleotide == "A":
                mRNA=mRNA+"U"
            elif nucleotide == "C":
                 mRNA=mRNA+"G"
            elif nucleotide == "G":
                 mRNA=mRNA+"C"
            elif nucleotide == "T":
                 mRNA=mRNA+"A"

    print("mRNA: " + mRNA)

    protein = ""
    i = 0

    while i < len(mRNA):
        codon = mRNA[i] + mRNA[i+1] + mRNA[i+2]
        AminoAcid=CodonChart[codon]
        if protein == "":
            protein = AminoAcid
        else:
            protein = protein + " - " + AminoAcid
        i = i + 3
    print(protein)

CodonChart = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

romeoDNA="TACCATCATCATCATCATATC"
habibiDNA="TACACGTAGCTACGATAGATC"

MakeProtein(romeoDNA)
MakeProtein(habibiDNA)
