def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    sml = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    big = [x for x in array if x > pivot]

    return quicksort(sml) + mid + quicksort(big)


lista_do_posortowania = [1, 2, 4, 10, 5, 6, 20, 14, 15]
print("Lista przed posortowaniem: ", lista_do_posortowania)
posortowana_lista = quicksort(lista_do_posortowania)
print("Lista po sortowaniiu: ", posortowana_lista)
