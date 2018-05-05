import math

preHash = hash(input("Enter your password: "))

myHash = preHash * float((preHash - (preHash % 9)))

finishedHash = hash(myHash) / (10 ** 10)

print(myHash)
print(preHash)
