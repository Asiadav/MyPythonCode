q1=1
q2=2
q3=3
q4=4
q5=5
q6=6




from random import shuffle

Qlist = [q1,q2,q3,q4,q5,q6]
shuffle(Qlist)
x = Qlist.pop()
print(x)