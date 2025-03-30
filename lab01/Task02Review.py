"""
File55. Дана строка S0, целое число N (≤ 4) и N файлов целых чисел с именамиS1, …, SN. Объединить
их содержимое в новом файле-архиве с именем S0, последовательно записываявнего следующие данные:
размер (число элементов) первого исходного файла и все элементы этого файла, размер второго
исходного файла и все его элементы, …, размер N-го исходного файла и все его элементы.
"""


import random


def generate_input_files(num_files: int) -> None:
    """
    Создает N бинарных файлов с именами S1.bin, S2.bin, ..., SN.bin.
    Каждый файл содержит случайное количество чисел (1-5) от 0 до 9.
    """
    for file_number in range(1, num_files + 1):
        elements_count = random.randint(1, 5)
        data = [f"{random.randint(0, 9)}\n".encode() for _ in range(elements_count)]
        with open(f"S{file_number}.bin", "wb") as file:
            file.writelines(data)


def merge_files_to_archive(output_filename: str, num_files: int) -> None:
    """
    Объединяет N файлов (S1.bin, S2.bin, ..., SN.bin) в архив <output_filename>.bin.
    Формат архива: размер файла + его элементы для каждого файла.
    """
    with open(f"{output_filename}.bin", "wb") as archive:
        for file_number in range(1, num_files + 1):
            # Читаем данные текущего файла
            with open(f"S{file_number}.bin", "rb") as file:
                elements = file.readlines()

            # Записываем размер файла как текстовую строку в байтах
            archive.write(f"{len(elements)}\n".encode('utf-8'))

            # Записываем сами элементы
            archive.writelines(elements)


def main():
    S0: str = input("Введите имя выходного файла (S0): ")

    while True:
        try:
            n: int = int(input("Введите N (1 <= N <= 4): "))
            if 1 <= n <= 4:
                break
            print("Error: N must be between 1 and 4.")
        except ValueError:
            print("Error: Invalid input. Expected integer.")

    generate_input_files(num_files = n)  # Создает S1.bin, S2.bin, ..., SN.bin
    merge_files_to_archive(
        output_filename = S0,
        num_files = n
    )  # Читает S1-SN.bin и пишет результат в <S0>.bin


if __name__ == "__main__":
    main()
