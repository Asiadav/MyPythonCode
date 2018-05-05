import string

intab = "abcdefghijklmnopqrstuvwxyz"

outtab = "cdefghijklmnopqrstuvwxyzab"


original = "map"

x = ''.maketrans(intab,outtab)


x = original.translate(x)
print(x)