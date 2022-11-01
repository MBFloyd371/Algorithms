def Average(lst):
    lst.copy()
    mean = (sum(lst) / len(lst))
    int(mean)
    print(mean)
    lst = [ele for ele in lst if ele < mean]
    return lst


line = [1, 3, 5, 6, 4, 10, 2, 3]
average = Average(line)
print(average)