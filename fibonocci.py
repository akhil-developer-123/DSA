#Write a program to print the Fibonacci sequence up to the nth term.
# 0 1 1 2 3 5 8 13 21 34


def fibonocci(n):
    first, second = 0, 1
    if n == 0:
        return []
    elif n == 1:
        return [first]
    elif n == 2:
        return [first, second]
    else:  
        result = [first, second]
        remaining_numbers = n - 2
        while remaining_numbers > 0:
            third = first + second
            remaining_numbers -= 1
            result.append(third)
            first = second
            second = third
        return result

result = fibonocci(10)
print(result)
result = fibonocci(5)
print(result)
result = fibonocci(1)
print(result)
