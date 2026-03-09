class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class BinTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return
        cur_node = self.root
        while True:
            if value <= cur_node.value:
                if cur_node.left is None:
                    cur_node.left = new_node
                    new_node.parent = cur_node
                    return
                cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = new_node
                    new_node.parent = cur_node
                    return
                cur_node = cur_node.right

    def insert_recursive(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return
        if value <= cur_node.value:
            if cur_node.left is None:
                cur_node.left = new_node
                new_node.parent = cur_node
                return
            self.insert_recursive(cur_node.left.value)
        else:
            if cur_node.right is None:
                cur_node.right = new_node
                new_node.parent = cur_node
                return
            cur_node = cur_node.right

    def get_parent(self, value):
        target_node = self.search(value)
        if target_node and target_node.parent:
            return target_node.parent.value
        return None

    #Метод показывает путь от заданного узла до корня
    def path_to_root(self, value):
        node = self.search(value)
        path = []
        while node:
            path.append(node.value)
            node = node.parent
        return path

    #Прямой обход (pre‑order): корень → левое поддерево → правое поддерево
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    def _preorder_recursive(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    def _inorder_recursive(self, node, result):
        if node is None:
            return
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    def _postorder_recursive(self, node, result):
        if node is None:
            return
        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)

    def _get_min_node(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node

    def _get_max_node(self, node):
        if not node:
            return None
        while node.right:
            node = node.right
        return node
    #Поиск минимального значения
    def get_min(self):
        min_node = self._get_min_node(self.root)
        if min_node is None:
            return None
        return min_node.value
    #Поиск максимального значения
    def get_max(self):
        max_node = self._get_max_node(self.root)
        if max_node is None:
            return None
        return max_node.value

    #Нахождение следующего по возрастанию
    def get_successor(self, value):
        node = self.search(value)
        if node is None:
            return None
        if node.right:
            successor_node = self._get_min_node(node.right)
            if successor_node is None:
                return None
            else:
                return successor_node.value

        while node.parent and node == node.parent.right:
            node = node.parent
        if node.parent is None:
            return None
        else:
            return node.parent.value
#исправить
    def remove(self, value):
        node = self.search(value)

        if node is None:
            return None

        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            return

        elif node.left is None or node.right is None:
            child = node.left if node.left else node.right
            if node.parent is None:
                node.parent = node.left
                node.left.parent = node.parent
            elif node.right:
                node.parent = node.right
                node.right.parent = node.parent

        elif node.left and node.right:
            successor = self._get_min_node(node.right)
            node.value = successor.value
            if successor.right is None:
                if successor.parent.left == successor:
                    successor.parent.left = None
                else:
                    successor.parent.right = None
            else:
                if successor.parent.left == successor:
                    successor.parent.left = successor.right
                else:
                    successor.parent.right = successor.right
                successor.right.parent = successor.parent

    def _right_rotate(self, y):
        x = y.right
        y.right = x.left
        if y.parent is not None:
            if y.parent.right == y:
                y.parent.right = x
            else:
                y.parent.left = x
        x.parent = y.parent
        y.parent = x
        x.left = y
        return x

    def _left_rotate(self, x):
        y = x.left
        x.left = y.right
        if x.parent is not None:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        y.parent = x.parent
        x.parent = y
        y.right = x
        return y







