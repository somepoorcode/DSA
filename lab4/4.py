def dfs(graph, visited, vertex, component):
    visited[vertex] = True  # Помечаем вершину как посещенную
    component.append(vertex)  # Добавляем текущую вершину к компоненте связности
    for neighbor in range(len(graph)):  # Рекурсивно вызываем dfs для всех
        # смежных с текущей вершин, если они еще не были посещены
        if graph[vertex][neighbor] == 1 and not visited[neighbor]:
            dfs(graph, visited, neighbor, component)


def find_connected_components(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices  # Инициализируем список посещенных вершин
    components = []  # Инициализируем список компонент связности

    for vertex in range(num_vertices):  # Для каждой вершины, которая еще не была посещена,
        # запускаем обход в глубину (DFS) и добавляем компоненту связности
        if not visited[vertex]:
            component = []
            dfs(graph, visited, vertex, component)
            components.append(component)

    return components


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = []
        max_length = max(len(line.strip()) for line in lines)
        for line in lines:  # Преобразуем строки из файла в матрицу смежности, дополняя недостающие нули
            row = list(map(int, (line.strip().ljust(max_length, '0'))))
            graph.append(row)
    return graph


filename = 'input.txt'
graph = read_graph_from_file(filename)
components = find_connected_components(graph)

with open('output.txt', 'w') as output_file:
    output_file.write(f"Количество компонент связности: {len(components)}\n")
    for i, component in enumerate(components, 1):
        output_file.write(f"Компонент связности {i}: {component}\n")

print("Результат записан в файл 'output.txt'.")
