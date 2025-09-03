def find_element(array):
    n = len(array)
    smallest = array[0]
    index_smallest = 0
    for i in range(1, n):
        if array[i] < smallest:
            smallest = array[i]
            index_smallest = i    
    return index_smallest