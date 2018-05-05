x = float(input("How many characters would you like too check for? "))
f = open('attempted passwords.txt','w')
if x>= 6:
    print("no")
    quit()
if x>= 1:
    for i in range(33,127):
        hackchar1 = i
        i++1
        print(chr(hackchar1))
        f.write(chr(hackchar1)+'\n')
if x>= 2:
    for p in range(33,127):
        hackchar2 = p
        for i in range(33,127):
            hackchar1 = i
            i++1
            print(chr(hackchar2)+chr(hackchar1))
            f.write(chr(hackchar2)+chr(hackchar1)+'\n')
if x>= 3:
    print("no longer displayiing combinations, check file")
    for o in range(33,127):
        hackchar3 = o
        for p in range(33,127):
            hackchar2 = p
            for i in range(33,127):
                hackchar1 = i
                i++1
                f.write(chr(hackchar3)+chr(hackchar2)+chr(hackchar1)+'\n')

if x>= 4:
    for u in range(33,127):
        hackchar4 = u
        for o in range(33,127):
            hackchar3 = o
            for p in range(33,127):
                hackchar2 = p
                for i in range(33,127):
                    hackchar1 = i
                    i++1
                    f.write(chr(hackchar4)+chr(hackchar3)+chr(hackchar2)+chr(hackchar1)+'\n')
if x>= 5:
    for y in range (33, 127):
        hackchar5 = y
        for u in range(33,127):
            hackchar4 = u
            for o in range(33,127):
                hackchar3 = o
                for p in range(33,127):
                    hackchar2 = p
                    for i in range(33,127):
                        hackchar1 = i
                        i++1
                        f.write(chr(hackchar5)+chr(hackchar4)+chr(hackchar3)+chr(hackchar2)+chr(hackchar1)+'\n')
f.close()