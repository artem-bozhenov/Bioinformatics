#Поиск подстроки в строке наивным способом, выводится первая найденная
def Naive_SubStrCmp(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if pattern[j] != text[i + j]:
                break
        else:
            return True
    return False

