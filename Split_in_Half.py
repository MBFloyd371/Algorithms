def split(s):
    print(s)
    half, string = divmod(len(s), 2)
    s = s[:half + string], s[half + string:]
    print(s)
    s = list(s)
    for i in range(0, len(s) - 1):
        s = s[-1:] + s[1:-1] + s[:1]


    return ''.join(s)

print(split('bbbbbcaaaaa'))