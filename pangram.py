def pangram(wor):
    alphabets={}
    wor=wor.upper()
    words=wor.split()
    for word in words:
        for letter in word:
            if letter not in alphabets.keys():
                alphabets[letter]=1
            else:
                 alphabets[letter]+=1
    if len(alphabets.keys())==26:
        print 'pangram'
    else:
        print 'not pangram'
    return


def main():
    word=raw_input('Enter the sentence  ')
    pangram(word)
    return



if __name__=='__main__':
    main()
