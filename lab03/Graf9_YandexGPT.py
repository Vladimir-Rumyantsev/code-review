def find_routes(k1, k2, l, m):
    n = len(m)
    routes = []

    def dfs(current, target, remaining_stops, path):
        if remaining_stops == 0:
            if current == target:
                routes.append(path + [target])
            return

        for i in range(n):
            if m[current][i] == 1 and i not in path:
                dfs(i, target, remaining_stops - 1, path + [current])

    dfs(k1 - 1, k2 - 1, l, [])
    return routes

def main():
    with open("FileName1", "r") as file:
        n = int(file.readline())
        matrix = [list(map(int, file.readline().split())) for _ in range(n)]

    k1, k2, l = map(int, input("Введите номера городов K1 и K2, а также количество пересадок L: ").split())
    routes = find_routes(k1, k2, l, matrix)

    with open("FileName2", "w") as output_file:
        if routes:
            output_file.write(f"{len(routes)}\n")
            for route in sorted(routes):
                output_file.write(" ".join(map(str, [i + 1 for i in route])) + "\n")
        else:
            output_file.write("-1\n")

if __name__ == "__main__":
    main()
