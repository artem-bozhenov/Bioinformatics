from collections import deque

#Класс для описания вершин.
class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None

#Класс для описания рёбер. Ребру записываются вершины, которые оно соединяет. Ребру задаётся цвет.
class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.color = "white"

class graph:
    def __init__(self):
        self.all_vertices = []  # Хранит все вершины графа

    def wide_search(self, vertices):
    #Функция для запуска поиска в ширину (BFS) для всех вершин графа.
    #vertices — список всех вершин графа.
        for v in vertices:
            if v.color == "white":
                self.vertex_wide_search(v)

    def vertex_wide_search(self, vertex):
        """
        Функция для выполнения BFS, начиная с заданной вершины.
        vertex — начальная вершина для поиска.
        """
        # Инициализируем очередь
        q = deque()

        # Добавляем начальную вершину в очередь и меняем её цвет на серый
        q.append(vertex)
        vertex.color = "gray"

        # Пока очередь не пуста
        while q:
            # Извлекаем вершину из очереди
            v = q.popleft()

            # Меняем цвет вершины на чёрный (обработана)
            v.color = "black"
            vertex.distance = 0
            vertex.parent = None

            # Проходим по всем соседям вершины v
            for w in v.neighbours:
                # Если сосед ещё не посещён (цвет белый), добавляем его в очередь и меняем цвет на серый
                if w.color == "white":
                    q.append(w)
                    w.color = "gray"
                    w.distance = v.distance + 1
                    w.parent = v

    def _reset_vertex_states(self):
        for vertex in self.all_vertices:
            vertex.color = "white"

    def find_shortest_path(self, start_vertex, end_vertex):
        self._reset_vertex_states()
        self.vertex_wide_search(start_vertex)

        if end_vertex.color == "white":
            return None

        path = []
        current_vertex = end_vertex

        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = current_vertex.parent

        path.reverse()
        return path

    def depth_search(self, vertices):
        for v in vertices:
            self._reset_vertex_states(v)
        for v in vertices:
            if v.color == 'white':
                self.vertex_depth_search(v)

    def vertex_depth_search(self, v):
        v.color = 'grey'
        for w in v.neighbours:
            if w.color == 'white':
                self.vertex_depth_search(w)
        v.color = 'black'

    #Определяет, есть ли хотя бы один цикл в графе
    def is_cycle(self, vertices):
        return self.depth_search_cycle(vertices)

    def depth_search_cycle(self, vertices):
        for v in vertices:
            self._reset_vertex_states(v)
        for v in vertices:
            if v.color == 'white':
                if self.vertex_depth_search_cycle(v):
                    return True
        return False

    def vertex_depth_search_cycle(self, v):
        v.color = 'grey'
        for w in v.neighbours:
            if w.color == 'white':
                self.vertex_depth_search_cycle(w)
            elif w.color == 'grey':
                return True
        v.color = 'black'
        return False

    def components_wide_search(self, vertices):
        components_list = []
        for v in vertices:
            if v.color == "white":
                component = self.vertex_wide_search(v)
                components_list.append(component)
        return components_list

    def components_vertex_wide_search(self, vertex):
        q = deque()
        component = []
        q.append(vertex)
        vertex.color = "gray"
        while q:
            v = q.popleft()
            v.color = "black"
            component.append(v)
            vertex.distance = 0
            vertex.parent = None
            for w in v.neighbours:
                if w.color == "white":
                    q.append(w)
                    w.color = "gray"
                    w.distance = v.distance + 1
                    w.parent = v
        return component

    #Топологическая сортировка
    def topological_sort(self, vertices):
        sorted_graph = []
        for v in vertices:
            self._reset_vertex_states(v)
        for v in vertices:
            if v.color == 'white':
                component_order = self.topological_vertex_depth_search(v)
                sorted_graph.extend(component_order)
        return sorted_graph

    def topological_vertex_depth_search(self, v):
        vertex_list = []
        v.color = 'grey'
        for w in v.neighbours:
            if w.color == 'white':
                self.topological_vertex_depth_search(w)
            elif w.color == 'grey':  # Проверка на цикл
                raise ValueError("Graph contains a cycle, topological sort impossible.")
        v.color = 'black'
        vertex_list.append(v)
        return vertex_list[::-1]

    #Нахождение минимального пути по весам рёбер между 2-мя вершинами
    def DinProg(self, start, stop):
        # Топологическая сортировка вершин
        v = self.topological_sort()

        # Индексы начальной (B) и конечной (E) вершин
        istart, istop = -1, -1

        # Находим индексы вершин B и E в отсортированном списке
        for i in range(len(v)):
            if v[i] == start:
                istart = i
            if v[i] == stop:
                istop = i

        # Если конечная вершина идёт раньше начальной — пути нет
        if istart < istop:
            return "no path"

        # Инициализируем веса вершин
        for vertex in v:
            vertex.weight = float('inf')  # Бесконечность по умолчанию

        # Вес начальной вершины равен 0
        v[istart].weight = 0

        # Проходим по вершинам от B до E
        for i in range(istart + 1, istop + 1):
            v[i].weight = float('inf')  # Инициализируем вес как бесконечность

            # Для каждой предыдущей вершины проверяем возможность обновления веса
            for w in v[i].previous:
                ww = w.weight + weight(w, v[i])  # Суммарный вес пути через w

                # Если найден более короткий путь — обновляем вес и родителя
                if ww < v[i].weight:
                    v[i].weight = ww
                    v[i].pi = w  # pi — родительская вершина

        # Восстанавливаем путь от E до B
        path = []
        w = stop

        while w != start:
            path.append(w)
            w = w.pi  # Переходим к родительской вершине

        path.append(start)  # Добавляем начальную вершину
        path.reverse()  # Разворачиваем путь в правильном порядке

        return path

    """
    Эйлеров путь (эйлерова цепь) — путь в графе, проходящий по каждому ребру ровно один раз. При этом путь может быть незамкнутым.

    Эйлеров цикл — частный случай эйлерова пути: замкнутый путь, проходящий через каждое ребро графа ровно по одному разу (начинается и заканчивается в одной вершине).

    Эйлеров граф — граф, содержащий эйлеров цикл.

    Полуэйлеров граф — граф, в котором есть эйлеров путь, но нет эйлерова цикла.                 
    
    Эйлеров цикл существует в связном ориентированном графе только если для каждой вершины количество входящих рёбер 
    равно количеству выходящих (индекс вершины = 0). Это необходимое и достаточное условие.
    
    Эйлеров цикл существует в связном неориентированном графе только если для каждой вершины количество примыкающих рёбер -
    чётное число (вершины имеют чётную степень).
    
    Эйлеров путь в ориентированном графе существует, если он слабо связан(был бы связным, если игнорировать ориентацию у рёбер) и
    имеет ровно 2 вершины с неравным количеством входящих и исходящих рёбер: начальная вершина(выходит на 1 ребро больше, чем входит),
    конечная вершина(входит на 1 ребро больше, чем выходит)
    
    Эйлеров путь в связном неориентированном графе существует, если у него не более 2-х вершин с нечётной степенью.
    """
    def euler_cycle(self, vertex):
        l = list()

        while True:
            l1 = list()
            self._simple_cycle(vertex, l1)
            l.insert(l1, vertex)
            for i in range(len(l)):
                if l[i].color == 'white':
                    break
            while vertex:
                return l

    def _simple_cycle(self, l1):
        l1.append(vertex)

        for e in edges



    

