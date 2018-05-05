while True:
    operand1 = input("first operand: ")
    try:
        operand1 = float(operand1)
    except ValueError:
        print("that is not a number")
        break
    a = 0
    operator = input("operator: ")
    if operator == '+':
        a = 1
    elif operator == '-':
        a = 1
    elif operator == '*':
        a = 1
    elif operator == '/':
        a = 1
    elif a == 0:
        print("that is not an available operator")
        break
    operand2 = input("second operand: ")
    try:
        operand2 = float(operand2)
    except ValueError:
        print("that is not a number")
        break
    if operator == '+':
        x = operand1 + operand2
        print (x)
    if operator == '-':
        x = operand1 - operand2
        print (x)
    if operator == '*':
        x = operand1 * operand2
        print (x)
    if operator == '/':
        x = operand1 / operand2
        print (x)
    yn = input("again? (y/n) ")
    if yn == 'y':
        continue
    else:
        break