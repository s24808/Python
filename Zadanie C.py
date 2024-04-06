def quicksort(array=None):
    if array is None:
        array = [10, 20, 12, 13, 16, 30, 50, 41]
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    sml = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    big = [x for x in array if x > pivot]

    return quicksort(sml) + mid + quicksort(big)
