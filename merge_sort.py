def mergeSort(L, descending = True):
    result = []
    if len(L) == 1:
        return L
    mid = len(L) // 2
    teilliste1 = mergeSort(L[:mid])
    teilliste2 = mergeSort(L[mid:])
    x, y = 0, 0
    while x < len(teilliste1) and y < len(teilliste2):
        if teilliste1[x] < teilliste2[y]:
            result.append(teilliste2[y])
            y = y + 1
        else:
            result.append(teilliste1[x])
            x = x + 1
    result = result + teilliste1[x:]
    result = result + teilliste2[y:]
    if descending == True :
        return result
    else:
        result.reverse()
        return result

test_list = [4, 6, 3, 1]
print(mergeSort(test_list))




