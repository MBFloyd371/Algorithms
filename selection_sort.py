def selection_descending(array):
    for i in range(len(array)):
        max_index = i
        for j in range(i+1, len(array)):
            if array[j] > array[max_index]:
                max_index = j
                print(array)
                array[i],array[max_index] = array[max_index],array[i]
                array = sorted(array, reverse=True)
                return array

lst = [30, 10, 50, 40 ]
print(selection_descending(lst))

