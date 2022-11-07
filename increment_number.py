def increment_number(digits):
    index = len(digits) - 1
    while (index >= 0 and digits[index] == 9):
        digits[index] = 0
        index -= 1
    if (index < 0):
        digits.insert(0, 1)
    else:
        digits[index] += 1
        return digits

list = [1,2,9]
print(increment_number(list))
