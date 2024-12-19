num1 = int(input('Enter the first number:- '))
num2 = int(input('Enter the second number:- '))
opr = input("Enter the Operator:- ")

if opr == '+':
    print(num1 + num2)
elif opr == '-':
    print(num1 - num2)
elif opr == '*':
    print(num1 * num2)
elif opr == '/':
    print(num1 / num2)
else:
    print('Invalid Operator or Number')

# ***** only IF use to make a calculator *****

num1 = int(input("Enter the number:- "))
num2 = int(input("Enter the second number"))
opr = input("Enter the Operator:- ")

if opr == '+':
    print(num1 + num2)
if opr == '-':
    print(num1 - num2)
if opr == '*':
    print(num1 * num2)
if opr == '/':
    print(num1 / num2)

if opr != '+' and opr != '-' and opr != '*' and opr != '/':
    print("Invalid Operator")