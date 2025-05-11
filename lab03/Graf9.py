def readMatrixFromFile(file_name: str):
    with open(file_name, 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().strip().split()))
            matrix.append(row)


def main():
    try:
        readMatrixFromFile("FileName1.txt")
    except ValueError:
        print("Не удалось считать FileName1.txt. В файле должны быть только целые числа")

    try:
        k1 = int(input().strip())
        k2 = int(input().strip())
        l = int(input().strip())
    except ValueError:
        print("Не удалось считать FileName1.txt. В файле должны быть только целые числа")


if __name__ == "__main__":
    main()
