# Find max number from 3 values

def max_number(a, b, c):
    if a > b and a > c:
        print(f"Maximum is {a}")
    elif b > c and b > a:
        print(f"Maximum is {b}")
    elif c > a and c > b:
        print(f"Maximum is {c}")
    else:
        print(f"Maximum is {a}")


result = max_number(300, 600, 900)
print(result)

