#Дан бинарный файл целых чисел. Продублировать в нем все элементы с нечетными номерами.
import struct

def duplicate_odd_indexed_elements(input_filename, output_filename):

    try:
        numbers = []
        with open(input_filename, 'rb') as infile:
            index = 0
            while True:
                data = infile.read(4)  # Читаем 4 байта (размер int)
                if not data:
                    break
                number = struct.unpack('i', data)[0]  # Распаковываем int
                numbers.append(number)

                if index % 2 == 0:  # *Четный индекс* (для дублирования нечетного элемента)
                    numbers.append(number)  # Дублируем элемент

                index += 1

        with open(output_filename, 'wb') as outfile:
            for number in numbers:
                data = struct.pack('i', number)  # Упаковываем int в байты
                outfile.write(data)

        print(f"Файл {input_filename} успешно обработан. Результат сохранен в {output_filename}")

        # Получаем содержимое исходного файла в виде строки
        with open(input_filename, 'rb') as infile:
            original_numbers = []
            while True:
                data = infile.read(4)
                if not data:
                    break
                number = struct.unpack('i', data)[0]
                original_numbers.append(number)
        original_string = ' '.join(map(str, original_numbers))

        # Получаем содержимое обработанного файла в виде строки
        with open(output_filename, 'rb') as outfile:
            processed_numbers = []
            while True:
                data = outfile.read(4)
                if not data:
                    break
                number = struct.unpack('i', data)[0]
                processed_numbers.append(number)
        processed_string = ' '.join(map(str, processed_numbers))

        return original_string, processed_string

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_filename} не найден.")
        return None, None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None, None

# Пример использования:
input_file = "celyy.bin"
output_file = "celyy2.bin"

original_string, processed_string = duplicate_odd_indexed_elements(input_file, output_file)

if original_string and processed_string:
    print("Содержимое исходного файла в виде строки:")
    print(original_string)
    print("Содержимое обработанного файла в виде строки:")
    print(processed_string)