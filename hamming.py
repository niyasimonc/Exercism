def hamming_diff(dna1,dna2):
    dna1=dna1.upper()
    dna2=dna2.upper()
    c=0
    if len(dna1)==len(dna2):
       for i in range(len(dna1)):
           if dna1[i]!=dna2[i]:
               c+=1
    else:
       print 'not in same lenth'
    return c
        


def main():
    dna1=raw_input('Enter first dna ')
    dna2=raw_input('Enter 2nd dna  ')
    h=hamming_diff(dna1,dna2)
    print 'Hamming difference is ',h
    return


if __name__=='__main__':
    main()
