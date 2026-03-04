class ListNode:
    #Узел односвязного списка
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    #Односвязный список
    def __init__(self):
        self.head = None
        self.size = 0

    #Проверяе пуст ли список
    def is_empty(self):
        return self.head is None

    #Добавление элемента в конец списка
    def append(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.size += 1

    #Добавление элемента в начало списка
    def prepend(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    #Вставка элемента со значением value по индексу
    def insert(self, index, value):
        # Проверка границ
        if index < 0 or index > self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size}]")

        new_node = ListNode(value)

        # Вставка в начало (index == 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # Ищем узел перед позицией вставки
            current = self.head
            for _ in range(index - 1):
                current = current.next

            # Вставляем новый узел
            new_node.next = current.next
            current.next = new_node

        self.size += 1


    #Удаление первого найденного элемента со значением value из списка
    def delete(self, value):
        if self.is_empty():
            return False

        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True

        cur_node = self.head
        while cur_node.next and cur_node.next.value != value:
            cur_node = cur_node.next

        if cur_node.next:
            cur_node.next = cur_node.next.next
            self.size -= 1
            return True
        else:
            return False

    #Проверяем наличие/отсутствие элемента в списке
    def find(self, value):
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:
                return True
            cur_node = cur_node.next
        return False

    #Показывает количество элементов в списке
    def get_size(self):
        return self.size

    #Выводит список в виде строки
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements) if elements else "Empty list"

    #Преобразует список в list()
    def to_list(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(cur_node.value)
            cur_node = cur_node.next
        return elements
