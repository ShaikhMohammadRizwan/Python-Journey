# # Q1 1, 2, 3, 4, 5.
#
# for i in range(1, 6):
#     print(i, end=" ")
#
# # Q2. Print Squares of Numbers from 1 to 5...
# print("")
# for i in range(1, 6):
#     print(i ** 2, end=" ")
#
# # Q3. Print Even Numbers from 1 to 10
# print("")
#
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, end=" ")
#
# # Q4. WAP to calculate Sum of Number from 1 to 10
# print("")
#
# total = 0
# for i in range(1, 10):
#     total += i
# print(f"Sum of {total}")
#
# # Q5. Write a Programm to Print the word "Python" in reverse using a for Loop
#
# char = "Python"
#
# for i in range(len(char) -1, -1, -1):
#     print(char[i], end=" ")
#
# print("")
# word = "JavaScript"
#
# for i in range(len(word) -1, -1, -1):
#     print(word[i], end=" ")
#
# # Q6. Count vowels in a string
# print(" ")
# vowels = "a, e, i, o, u"
# words = 'Educations'
# count = 0
#
# for char in words:
#     if char in vowels:
#         count += 1
# print('Total number of vowels in', count)

# Q7. WAP to print a Fibonacci Sequence up to 10 Terms
print("")

a = 0
b = 1
print(a, b, end=" ")

for i in range(10):
    fib_sum = a + b
    print(fib_sum, end=" ")
    a, b = b, fib_sum


# Q8. WAP to calculate the factorial of a given number such as 5
print(" ")

n = 6
factorial = 1

for i in range(1, n+1):
    factorial *= i
print(f"The Factorial of {n} is {factorial}")


# Q9. WAP to check if a givem=n number, such as 7 is prime number
print(" ")

num = 2
