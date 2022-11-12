def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                alist = sorted(alist, reverse=True)
                return alist

lst = [4, 2, 6, 3, 1]
print(bubbleSort(lst))