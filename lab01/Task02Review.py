"""
File55. Дана строка S0, целое число N (≤ 4) и N файлов целых чисел с именамиS1, …, SN. Объединить
их содержимое в новом файле-архиве с именем S0, последовательно записываявнего следующие данные:
размер (число элементов) первого исходного файла и все элементы этого файла, размер второго
исходного файла и все его элементы, …, размер N-го исходного файла и все его элементы.
"""


def create_test_file(filename: str, data):
    with open(filename, "wb") as f:
        f.writelines(data)


def read_binary_file(filename: str):
    with open(filename, "rb") as f:
        return f.readlines()


def sozdati(S0, a):
    b = a + 1
    for i in range(1, b):
        mas = [
            b"1\n", b"2\n", b"3\n",
            b"4\n", b"5\n", b"6\n",
            b"7\n", b"8\n", b"9\n",
            b"10\n",
        ]
        nazw = S0 + str(i) + ".bin"
        create_test_file(filename=nazw, data=mas)


def otw(S0, a):
    b = a + 1
    m = []
    file_sizes = []
    for i in range(1, b):
        nazw = S0 + str(i) + ".bin"
        a = read_binary_file(nazw)
        for i in range(len(a)):
            m.append(a[i])
        file_sizes.append(len(a))

    nazw = S0 + "0" + ".bin"
    for i in range(len(file_sizes)):
        zap = bytes(str(file_sizes[i]), encoding="utf-8")
        zap += b"\n"
        for j in range(file_sizes[i]):
            zap += m[j]
            m = m[file_sizes[i]:]
        create_test_file(filename=nazw, data=zap)


if __name__ == "__main__":
    S0 = str(input("Введите строку S0: "))
    try:
        a = int(input("Введите число исходных файлов: "))
        sozdati(S0=S0, a=a)
        otw(S0=S0, a=a)
    except ValueError as e:
        print(f"Error: {e}")
