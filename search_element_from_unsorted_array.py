def func(arr, el, break_phrase):
    for i in range(len(arr)):
        if arr[i] == el:
            return i
    return break_phrase

func(arr, el, break_phrase)
