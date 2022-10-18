# When a user enters a number n, find the sum of all digits in all numbers from 1 to n

def sum_number(n):
    sum = 0

    while (n > 0):
        sum += int(n % 10)
        n = int(n / 10)

    return sum


number = 3434
result = sum_number(number)
print(result)












