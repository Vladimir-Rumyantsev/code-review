from itertools import permutations

# Пример содержимого файла FileName1
matrix_data = """
5
0 1 1 0 0
1 0 1 1 0
1 1 0 0 1
0 1 0 0 1
0 0 1 1 0
"""

# Разбор данных из строки
lines = matrix_data.strip().split("\n")
n = int(lines[0].strip())
adjacency_matrix = [[int(x) for x in line.split()] for line in lines[1:]]

# Параметры задачи
K1 = 1  # начальный город
K2 = 5  # конечный город
L = 2  # количество пересадок


# Функция для поиска маршрутов
def find_routes(n, adjacency_matrix, K1, K2, L):
    # Начальный город
    start = K1 - 1
    # Конечный город
    end = K2 - 1

    # Список для хранения найденных маршрутов
    routes = []

    # Рекурсивная функция для поиска маршрутов
    def dfs(current, path, transfers):
        # Если достигли конечного города с нужным числом пересадок
        if current == end and transfers == L:
            routes.append(list(path))
            return

        # Если пересадок больше чем нужно, выходим
        if transfers > L:
            return

        # Проходим по всем городам
        for neighbor in range(n):
            if adjacency_matrix[current][neighbor] == 1 and (len(path) == 0 or neighbor != path[-1]):
                path.append(neighbor + 1)
                dfs(neighbor, path, transfers + 1)
                path.pop()

    # Запускаем поиск
    dfs(start, [start + 1], 0)

    # Возвращаем отсортированные маршруты
    return sorted(routes)


# Поиск маршрутов
routes = find_routes(n, adjacency_matrix, K1, K2, L)

# Подготовка результатов для записи в файл
result_lines = [str(len(routes))] if routes else ["-1"]
result_lines += [" ".join(map(str, route)) for route in routes]

# Сохранение результатов в файл
output_path = 'FileName2.txt'
with open(output_path, 'w') as file:
    file.write("\n".join(result_lines))

# output_path