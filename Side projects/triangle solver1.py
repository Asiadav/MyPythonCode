import math
'''
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
A = float(input("m<A = "))
B = float(input("m<B = "))
C = float(input("m<C = "))


'''

def SAS():
        print("\nSAS\n")
        s1= float(input("first side = "))
        angle3 = float(input("angle = "))
        s2 = float(input("second side = "))

        rad = (angle3/ 180) * math.pi
        r = math.cos(rad)
        s3 = math.sqrt((s1**2 + s2**2) - (2*s1*s2*r))
        print("The third side is", s3)

        angle2 = math.asin((s2 * math.sin(rad)) / s3)
        angle2 = (angle2 * 180) / math.pi
        print("The second angle is", angle2)

        angle1 = 180 - (angle2 + angle3)
        print("The first angle is", angle1)
        findArea(s1, s2, angle3)



def SSS():
        print("\nSSS\n")
        s1= float(input("first side = "))
        s2 = float(input("second side = "))
        s3 = float(input("third side = "))

        rad = math.acos((s1**2 + s2**2 - s3**2) / (2 * s1 * s2))
        angle3 = (rad * 180) / math.pi
        print("The third angle is", angle3)

        rad = math.acos((s1**2 + s3**2 - s2**2) / (2 * s1 * s3))
        angle2 = (rad * 180) / math.pi
        print("The second angle is", angle2)

        angle1 = 180 - (angle3 + angle2)
        print("The first angle is", angle1)
        findArea(s1, s2, angle3)


def SSA():
        print("\nSSA\n")
        s1= float(input("first side (opposite angle) = "))
        s2 = float(input("second side = "))
        angle1 = float(input("angle (opposite side) = "))

        rad = (angle1 / 180) * math.pi
        angle2 = math.asin((s2 * math.sin(rad)) / s1)
        angle2 = (angle2 * 180) / math.pi
        print("The second angle is", angle2)

        angle3 = 180 - (angle1 + angle2)
        print("The third angle is", angle3)

        rad = (angle3/ 180) * math.pi
        r = math.cos(rad)
        s3 = math.sqrt((s1**2 + s2**2) - (2*s1*s2*r))
        print("The third side is", s3)
        findArea(s1, s2, angle3)


def AAS():
        print("\nAAS\n")
        angle1= float(input("first angle (opposite side) = "))
        angle2 = float(input("second angle = "))
        s1 = float(input("side (opposite angle) = "))

        angle3 = 180 - (angle1 + angle2)
        print("The third angle is", angle3)

        rad2 = (angle2/ 180) * math.pi
        rad = (angle1/ 180) * math.pi
        r2 = math.sin(rad2)
        r = math.sin(rad)
        s2 = (r2 * s1) / r
        print("The second side is", s2)

        rad = (angle3/ 180) * math.pi
        r = math.cos(rad)
        s3 = math.sqrt((s1**2 + s2**2) - (2*s1*s2*r))
        print("The third side is", s3)

        findArea(s1, s2, angle3)

def findArea(s1, s2, angle3):
        angle3 = (angle3 / 180) * math.pi
        area = (s1 * s2 * math.sin(angle3)) / 2
        print("The area is", area)


x = 1
while x == 1:
        try:
                print("1: AAS")
                print("2: SAS")
                print("3: SSA")
                print("4: SSS")

                choice = int(input(""))

                if choice == 1:
                        AAS()
                        i = input("again? (y/n)")
                        if i != 'y':
                                x = 0
                if choice == 2:
                        SAS()
                        i = input("again? (y/n)")
                        if i != 'y':
                                x = 0
                if choice == 3:
                        SSA()
                        i = input("again? (y/n)")
                        if i != 'y':
                                x = 0
                if choice == 4:
                        SSS()
                        i = input("again? (y/n)")
                        if i != 'y':
                                x = 0

        except:
                'try again'