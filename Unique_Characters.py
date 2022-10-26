def specialCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if (str[i] == str[j]):
                return False


    return True


print(specialCharacters('abcde'))
