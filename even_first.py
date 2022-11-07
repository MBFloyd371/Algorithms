def even_odd(lst):
    u = 0
    for i in range(len(lst)):
        if lst[u]%2!=0:
            pin = lst[u]
            lst.remove(lst[u])
            lst.append(pin)
        else:
            u+=1
    return lst


list =  [7, 3, 5, 6, 4, 10, 3, 2]
print(even_odd(list))

