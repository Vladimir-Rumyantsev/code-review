# Дан бинарный файл целых чисел. Продублировать в нем все элементы с нечетными номерами.
import struct


def read_binary_file(filename):
    numbers = []
    try:
        with open(filename, "rb") as file:
            while True:
                data = file.read(4)
                if not data:
                    break
                if len(data) != 4:
                    raise ValueError("Invalid data length.")
                number = struct.unpack('i', data)[0]
                numbers.append(number)
        return numbers
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None


def duplicate_odd_indexed_elements(input_filename, output_filename):

    try:
        numbers = []
        with open(input_filename, "rb") as infile:
            index = 0
            while True:
                data = infile.read(4)  # Читаем 4 байта (размер int)
                if not data:
                    break
                if len(data) != 4:
                    raise ValueError("Unexpected end of file or corrupted data.")
                number = struct.unpack('i', data)[0]  # Распаковываем int
                numbers.append(number)

                if index % 2 == 0:  # *Четный индекс* (для дублирования нечетного элемента)
                    numbers.append(number)  # Дублируем элемент

                index += 1

        with open(output_filename, "wb") as outfile:
            for number in numbers:
                data = struct.pack('i', number)  # Упаковываем int в байты
                outfile.write(data)

        print(f"File {input_filename} processed successfully. Result saved to {output_filename}.")

        # Получаем содержимое исходного файла в виде строки
        original_string = ' '.join(map(str, read_binary_file(filename=input_filename)))

        # Получаем содержимое обработанного файла в виде строки
        processed_string = ' '.join(map(str, read_binary_file(filename=output_filename)))

        return original_string, processed_string

    except FileNotFoundError:
        print(f"Error: The {input_filename} file was not found.")
        return None, None


if __name__ == "__main__":

    # Пример использования:
    input_file = "celyy.bin"
    output_file = "celyy2.bin"

    original_string, processed_string = duplicate_odd_indexed_elements(
        input_filename=input_file,
        output_filename=output_file
    )

    if original_string and processed_string:
        print(f"Содержимое исходного файла в виде строки: {original_string}")
        print(f"Содержимое обработанного файла в виде строки: {processed_string}")
