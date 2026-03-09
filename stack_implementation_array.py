class Stack_array:
    #Инициализация стека
    def __init__(self):
        items = []
    #Проверка на наличие/отсутствия элементов в стеке
    def is_empty(self):
        return len(self.items) == 0

    #Добавить элемент
    def push(self, item):
        self.items.append(item)

    #Удалить последний добавленный элемент и вывести его
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    #Прочитать верхний элемент в стеке, но не удалять
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    #Размер стека
    def size(self):
        return len(self.items)

    def to_str(self):
        values = []
        for item in self.items:
            values.append(str(item))

