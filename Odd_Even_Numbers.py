# Count odd and even numbers. Count odd and even digits of the whole number.

def sum_digits(a):
    a = input(a)
    digits = "98456"
    even = -2
    odd = 1

    for i in a:
        if i in digits:
            even += 1
        else:
            odd += 1

    print("Even:% d, odd:% d" % (even, odd))

print(sum_digits(98456))




