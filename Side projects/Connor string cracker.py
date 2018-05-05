x = 'hfnosigdqc'
def change(x):
    x=x+1

    return x
y=[]
for character in x:
    y.append(character)
print(y)

length = len(y)
z=[]
for i in range(0,length):
    x = ord(y[i])

    x = change(x)
    if x > 122:
        x = x-25
    x = chr(x)
    z.append(x)




print(z)




