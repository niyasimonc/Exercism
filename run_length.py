def encode(string):
    count=1
    prev = ''
    lst = []
    i=0
    for character in string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
        i+=1
        if i==len(string):
           lst.append((prev,count))  
    re=''
    for tup in lst  :
        re+=str(tup[1])+tup[0]
    
    return re




def main():
    string=raw_input('Enter the string  ')
    en_str=encode(string)
    print en_str
    return


if __name__=='__main__':
    main()

