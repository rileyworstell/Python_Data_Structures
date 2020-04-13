def bubbleSort(array):
    swaps = 0
    for j in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swaps += 1
        if swaps == 0:
            return array
    return array
