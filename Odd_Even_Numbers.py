# Count odd and even numbers. Count odd and even digits of the whole number.

def even_or_odd(n):
    even_count = 0
    odd_count = 0
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            even_count += 1
        else:
            odd_count += 1

        n = int(n / 10)

    print("Even count : ", even_count)
    print("\nOdd count : ", odd_count)

print(even_or_odd(3229967893))
