def sorted_array_insert(arr,el):
    left = 0
    right = len(arr)

    while left < right:
        m = (left+right) // 2
        if arr[m] >= el:
            right = m
        else:
            left = m + 1

    #добавим в конец 1 элемент, чтобы сдвинуть значения для вставки
    arr.append(0)

    #сдвинем все элементы, которые больше текущего, вправо
    for i in range(len(arr) - 1, left, -1):
        arr[i] = arr[i - 1]

    #вставим требуемый элемент
    arr[left] = el

    return arr

sorted_array_insert(arr, el)
