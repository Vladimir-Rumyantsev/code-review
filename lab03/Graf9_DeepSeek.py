def main():
    # Read input from FileName1
    with open('FileName1', 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().strip().split()))
            matrix.append(row)

    # Read K1, K2, L from stdin
    k1 = int(input().strip())
    k2 = int(input().strip())
    l = int(input().strip())

    # Validate input
    if k1 < 1 or k1 > n or k2 < 1 or k2 > n or l < 0:
        with open('FileName2', 'w') as f_out:
            f_out.write("-1\n")
        return

    paths = []

    if l == 0:
        if k1 == k2:
            paths = [[k1]]
        else:
            if matrix[k1 - 1][k2 - 1] == 1:
                paths = [[k1, k2]]
            else:
                paths = []
    else:
        required_length = l + 2  # number of cities

        def backtrack(current_path):
            if len(current_path) == required_length:
                if current_path[-1] == k2:
                    paths.append(current_path.copy())
                return
            current_city = current_path[-1]
            current_index = current_city - 1
            for next_city in range(1, n + 1):
                next_index = next_city - 1
                if matrix[current_index][next_index] == 1:
                    current_path.append(next_city)
                    backtrack(current_path)
                    current_path.pop()

        backtrack([k1])

    # Sort paths lexicographically
    paths.sort()

    # Write to FileName2
    with open('FileName2', 'w') as f_out:
        if not paths:
            f_out.write("-1\n")
        else:
            f_out.write(f"{len(paths)}\n")
            for path in paths:
                f_out.write(' '.join(map(str, path)) + '\n')


if __name__ == "__main__":
    main()
