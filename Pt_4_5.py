def all_paths(graph, start_point, end_point, path):
    path = path + [start_point]
    paths = []
    if start_point == end_point:
        return [path]
    if start_point not in graph:
        return []
    for current in graph[start_point]:
        new_paths = all_paths(graph, current, end_point, path)
        paths += new_paths
    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []
paths = all_paths(graph, start, end, path)
print("Все пути от вершины A до вершины F:", paths)
