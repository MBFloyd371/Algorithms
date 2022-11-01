def lowest_elements(lst):
    temp_lst = lst.copy()
    temp_lst.sort()
    return temp_lst[0:2]


list = [198, 3, 4, 9, 10, 9, 2]
print(lowest_elements(list))
