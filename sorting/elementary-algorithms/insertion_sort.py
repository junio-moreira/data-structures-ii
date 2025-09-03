def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave   