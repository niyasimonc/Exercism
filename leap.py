

def main():
    year=raw_input("Enter the year  ")
    if int(year)%4 ==0:
         if int(year)%100==0:
            if int(year)%400==0:
                print 'leap year'
            else:
                print 'not leap year'
         else:
             print 'leap year'
    else:
       print 'not leap year'

if __name__=='__main__':
    main()
