class ListNode:
    #Узел двухсвязного списка
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    #Двухсвязный список
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #Проверка пуст ли список
    def is_empty(self):
        return self.head is None

    #Добавление элемента в конец
    def append(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    #Добавление элемента в начало
    def prepend(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    #Удаление элемента
    def delete(self, data):
        #Удаляет первый узел с заданным значением
        current = self.head
        while current:
            if current.data == data:
                #Если узел единственный в списке
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                #Если удаляем головной узел
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None
                #Если удаляем хвостовой узел
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                #Если узел в середине
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                return True  #Элемент найден и удалён
            current = current.next
        return False  #Элемент не найден

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

    #Вывод списка от головы к хвосту
    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    #Вывод списка от хвоста к голове
    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return elements

