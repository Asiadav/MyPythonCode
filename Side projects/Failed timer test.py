import time
x = 0

for i in range(0,10):
    x = 10 - i
    time.sleep(1)
    print(x)
    f = open('timerValues.txt','w')
    f.write(str(x))
    f.close()
