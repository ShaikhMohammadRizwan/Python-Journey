# For Loop with Range in Python
#
# for n in range(5):
#     print(n)
#
# print("")
#
# for n in range(1,6):
#     print(n)
#
# print("")
#
# for i in range(1, 11):
#     print("2 x", i, "=", 2*i)
#
# print("")
#
# for i in range(10, 0, -1):
#     print(i)

# ***********Coding with Sagar **************
print("")
for i in range(1, 10):
    print(i)

print("")

#Q1 input 2 number LIst

m = int(input("Enter the Start Number:- "))
n = int(input("Enter the end Number:- "))
z = n + 1

for i in range(m, z):
    print(m)
    m += 1

#Q2. Reverse The Number of user input

a = int(input("Enter the Start Number:- "))
b = int(input("Enter the End Number:- "))
# c = b - 1

for i in range(a, b, -1):
    print(a)
    a -= 1

print("")

for i in range(1,101):
    if i % 3 == 0:
        print(i)

m = int(input("Enter the Number:- "))
n = int(input("Enter the Number:- "))
z = int(input("Enter the Divisor"))

for i in range(m, n):
    if i % z == 0:
        print(i)