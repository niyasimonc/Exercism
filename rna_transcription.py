def rna(dna):
    dna_nucli_compl={'G':'C','C':'G','T':'A','A':'U'}
    dna=dna.upper()
    rna=''
    for i in dna:
        rna+=dna_nucli_compl[i]
    print rna
    return


def main():
    dna=raw_input("Enter dna ")
    rna(dna)
    return


if __name__=='__main__':
    main()
