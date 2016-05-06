def wc(words):
    count={}
    for word in words:
        if word not in count.keys():
           count[word]=1
        else:
           count[word]+=1
    return count



def main():
    sentence=raw_input("Enter the sentence ")
    words=sentence.split()
    dic=wc(words)
    print dic
    return



if __name__=='__main__':
    main()
