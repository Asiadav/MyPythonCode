x = float(input("How many characters would you like too check for? "))
f = open('attempted passwords.txt','w')
myRange = list(range(33,38))+list(range(44,57))+list(range(64,65))+list(range(95, 123))
myRangeFirst = list(range(33,38))+list(range(44,57))+list(range(64,65))+list(range(65,95))+list(range(95,123))
if x>= 6:
    print("no")
    quit()
if x>= 1:
    for i in myRangeFirst:
        hackchar1 = i
        print(chr(hackchar1))
        f.write(chr(hackchar1)+'\n')
if x>= 2:
    for p in myRangeFirst:
        hackchar2 = p
        for i in myRange:
            hackchar1 = i
            print(chr(hackchar2)+chr(hackchar1))
            f.write(chr(hackchar2)+chr(hackchar1)+'\n')
if x>= 3:
    print("no longer displayiing combinations, check file")
    for o in myRangeFirst:
        hackchar3 = o
        for p in myRange:
            hackchar2 = p
            for i in myRange:
                hackchar1 = i
                f.write(chr(hackchar3)+chr(hackchar2)+chr(hackchar1)+'\n')

if x>= 4:
    for u in myRangeFirst:
        hackchar4 = u
        for o in myRange:
            hackchar3 = o
            for p in myRange:
                hackchar2 = p
                for i in myRange:
                    hackchar1 = i
                    f.write(chr(hackchar4)+chr(hackchar3)+chr(hackchar2)+chr(hackchar1)+'\n')
if x>= 5:
    for y in myRangeFirst:
        hackchar5 = y
        for u in myRange:
            hackchar4 = u
            for o in myRange:
                hackchar3 = o
                for p in myRange:
                    hackchar2 = p
                    for i in myRange:
                        hackchar1 = i
                        f.write(chr(hackchar5)+chr(hackchar4)+chr(hackchar3)+chr(hackchar2)+chr(hackchar1)+'\n')
f.close()
