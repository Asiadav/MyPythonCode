import time

primeDoc = open("Prime Numbers.txt","r")

prime_number = int(input("Which prime?"))


prime_check = 2
top_line = 0


while True:
    top_line += 1
    try:
        testForData = primeDoc.readline()
        print(testForData)
        if testForData == "":
            broke = true
        
        currentPrime = int(testForData[0:len(testForData)-1])
        
    except:
        #print(testForData)
        top_line += 1
        #print(top_line)
        break
    
if top_line > prime_number:
    print(top_line,prime_number)
    print(primeDoc.readline(prime_number))
    testForData = primeDoc.readline()
    testForData = primeDoc.readline()
    
    print(testForData)
    #currentPrime = int(testForData[0:len(testForData)-1])
    print(currentPrime)
    primeDoc.close()
    
else:
    prime_check = currentPrime + 2
    while top_line < prime_number:
        not_prime = False
        
        primeDoc = open("Prime Numbers.txt","r")
        
        for line in primeDoc:
            print(line)
            prime = int(line[0:len(line)-1])
            
            if prime_check % prime == 0:
                prime_check += 1            
                not_prime = True
        
        primeDoc.close()
        
        
        if not_prime == False:
            primeDoc = open("Prime Numbers.txt","a")
            
            prime_check_str = str(prime_check)
            primeDoc.write(prime_check_str)
            #primeDoc.write("\n")
            top_line += 1
            
            primeDoc.close()
            
print(currentPrime)
    

