"""
Questions
Write a program that prints "Hello, World!".
Create a program to swap two numbers without using a temporary variable.
Write a program to find the area of a circle with a given radius.
Take input from the user and display its data type.
Convert temperature from Celsius to Fahrenheit.
Write a program to check if a number is odd or even.
Create a program that takes three numbers and prints their average.
Write a program to find the largest of three numbers.
Write a program to calculate the factorial of a number.
Write a program to reverse a given string.
Loops
Write a program to print the first 10 natural numbers using a while loop.
Write a program to display the multiplication table of a given number.
Create a program to find the sum of numbers from 1 to 100 using a loop.
Write a program to print all even numbers between 1 and 50.
"""

#1
print("Hello, World!")

# 2a. Create a program to swap two numbers using a temporary variable
def swapWithTmp(x,y):
    tmp = x
    x = y
    y = x
    return [x,y]
#swapWithTmp(4,5)

# 2b. Create a program to swap two numbers without using a temporary variable
def swapWithoutTmp(x, y):
    x, y = y,x
    return [x,y]
#swapWithoutTmp(2,3)

#3. Write a program to find the area of a circle with a given radius.

def findAreaOfCircle(radius):
    pi = 3.14
    return 3.14 * (radius ** 2)
#findAreaOfCircle(10)

#4 Take input from the user and display its data type.
def findInputType():
    data = input("enter your input here")
    return type(data)
#findInputType()

#5 Convert temperature from Celsius to Fahrenheit.

def convertCelsiusToFahrenheit(celsius):
    return celsius * 9/5 + 32
#convertCelsiusToFahrenheit(32)

#6. Write a program to check if a number is odd or even.

def isEvenOrOdd(number):
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')
        
#isEvenOrOdd(5)
#isEvenOrOdd(4)
#isEvenOrOdd(100)

#7. Create a program that takes three numbers and prints their average.
def findAverageOfThreeNumbers(a, b, c):
    return (a+b+c) / 3
#findAverageOfThreeNumbers(1,2,3)

#8. Write a program to find the largest of three numbers.
def findLargestOfThreeNums(a, b, c):
    return max([a,b,c])
#findLargestOfThreeNums(1,2,3)

def findLargestOfThreeNumsApproach2(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c
#findLargestOfThreeNumsApproach2(1,2,3)
    
    
#9 Write a program to calculate the factorial of a number.
def factorial(num):
    if num < 0:
        print('invalid input')
        return
    if num <= 1:
        return 1
    return num * factorial(num-1)
    
#factorial(5)


# 10 Write a program to reverse a given string.

def reverseString(s):
    return s[::-1]
#reverseString("hello")

def reverseStringWithTwoPointers(s):
    # two pointer approach
    listOfChars = list(s)
    n = len(s)
    i,j = 0, n-1
    while i < j:
        listOfChars[i], listOfChars[j] = listOfChars[j], listOfChars[i]
        i += 1
        j -= 1
    return "".join(listOfChars)
#reverseStringWithTwoPointers("hello")

#11. Write a program to print the first 10 natural numbers using a while loop

def printFirstXNaturalNumbers(num=10):
    for i in range(1, num + 1):
        print(i)
#printFirstXNaturalNumbers()

# 12 Write a program to display the multiplication table of a given number.

def printMultiplicationTable(num):
    for i in range(10):
        print(f"{num} * {i} = {num * i}")

#printMultiplicationTable(2)

# 13. Create a program to find the sum of numbers from 1 to 100 using a loop.

def sumOfXNumbers():
    answer = 0
    for number in range(1, 101):
        answer += number
    return answer

# 14 Write a program to print all even numbers between 1 and 50.

def printEvenNumbers():
    for i in range(2, 50, 2):
        print(i)

        



