class ListNode:
    def __init__(self, value):
        #Узел односвязного списка
        self.value = value
        self.next = None

class Stack_LinkedList:
    #Инициализация стека
    def __init__(self):
        self.top = None
        self._size = 0

    #Проверка на пустоту стека
    def is_empty(self):
        return self.top is None

    #Добавление элемента сверху в стек
    def push(self, value):
        new_node = ListNode(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    #Удаление верхнего узла
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    #Вывод элемента сверху стека без его удаления
    def peek(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.top.value

    #Количество узлов в связном списке
    def size(self):
        return self._size

    #Отображение стека в виде строки
    def to_str(self):
        values = []
        current = self.top
        while current:
            values.append(str(current.value))
            current = current.next
        return "Stack: " + " -> ".join(values)
