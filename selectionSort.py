def selectionSort(array):
    for j in range(len(array)):
        for i in range(len(array)):
            if i < j:
                pass
            elif array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
                

    return array
