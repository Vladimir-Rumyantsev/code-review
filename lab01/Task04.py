# программа считывает данные об N учениках и записывает их в бинарный файл
# ввод: N (число записей), затем сведения об N учениках (Фамилия, Имя, Класс, Скорость чтения (int, 1 кл.) /
# Баллы за контрольную по математике (от 1 до 10, float, 2-3 кл.) /
# Баллы за итоговую аттестацию (от 1 до 100, float, 4 кл.))
# вывод: содержимое файла в виде таблицы

import struct

class student:
    def __init__(self, lastname, name, grade):
        self.lastname = lastname
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return f'{self.lastname:<15} {self.name:<12} {self.grade:<6}'
    
class first_grade_student(student):
    def __init__(self, lastname, name, grade, mark):
        super().__init__(lastname, name, grade)
        self.mark = mark
    
    def __str__(self):
        return super().__str__() + f' {self.mark:<20} {"-":<20} {"-":<20}'
    
class second_or_third_grade_student(student):
    def __init__(self, lastname, name, grade, mark):
        super().__init__(lastname, name, grade)
        self.mark = mark
    
    def __str__(self):
        return super().__str__() + f' {"-":<20} {self.mark:<20} {"-":<20}'

class fourth_grade_student(student):
    def __init__(self, lastname, name, grade, mark):
        super().__init__(lastname, name, grade)
        self.mark = mark
    
    def __str__(self):
        return super().__str__() + f' {"-":<20} {"-":<20} {self.mark:<20}'
    
def input_student():
    lastname = input('      Фамилия: ')
    name = input('      Имя: ')
    grade = input('      Класс от 1 до 4: ')
    # защита от дурака
    try:
        grade = int(grade)
        if not (1 <= grade <= 4):
            print('Введены некорректные данные, попробуйте снова.')
            return None
    except ValueError:
        print('Введены некорректные данные, попробуйте снова.')
        return None
    
    if grade == 1:
        mark = input('      Скорость чтения (кол-во слов/мин): ')
        try:
            mark = float(mark)
            if mark == int(mark) and mark >= 0:
                mark = int(mark)
                return first_grade_student(lastname, name, grade, mark)
            else:
                print('Введены некорректные данные, попробуйте снова.')
                return None
        except ValueError:
            print('Введены некорректные данные, попробуйте снова.')
            return None
            
    elif 2 <= grade <= 3:
        mark = input('      Оценка от 1 до 10 за итоговую школьную аттестацию: ')
        try:
            mark = float(mark)
            if (1 <= mark <= 10):
                return second_or_third_grade_student(lastname, name, grade, mark)
            else:
                print('Введены некорректные данные, попробуйте снова.')
                return None
        except ValueError:
            print('Введены некорректные данные, попробуйте снова.')
            return None
        
    elif grade == 4:
        mark = input('      Баллы от 1 до 100 за итоговую аттестацию: ')
        try:
            mark = float(mark)
            if (1 <= mark <= 100):
                return fourth_grade_student(lastname, name, grade, mark)
            else:
                print('Введены некорректные данные, попробуйте снова.')
                return None
        except ValueError:
            print('Введены некорректные данные, попробуйте снова.')
            return None
             
def write_bin(file, data):
    with open(file, "ab") as f:
        for student in data:
            # Кодируем и записываем строковые данные
            lastname_encoded = student.lastname.encode('utf-8')
            f.write(struct.pack('i', len(lastname_encoded)))
            f.write(lastname_encoded)

            name_encoded = student.name.encode('utf-8')
            f.write(struct.pack('i', len(name_encoded)))
            f.write(name_encoded)

            f.write(struct.pack('i', student.grade))

            # Записываем оценку в зависимости от класса
            if isinstance(student, first_grade_student):
                f.write(struct.pack('i', int(student.mark))) 
            else:
                f.write(struct.pack('f', float(student.mark)))  

def main():
    students = []
    # защита от дурака
    while True:
        n = input('Введите количество учеников для добавления сведений в базу данных: ')
        if n.isdigit() and float(n) == int(float(n)):
            n = int(n)
            break
        else:
            print('Введены некорректные данные, попробуйте снова.')
    
    # получаем данные об n учениках
    for _ in range(n):
        print()
        student = None
        while student is None:
            student = input_student()
        students.append(student)
        
    write_bin('3lab15.bin', students)
    
main()

def read_bin(file):
    with open(file, 'rb') as f:
        data = []
        while True:
            student = []
            len_str1 = f.read(4)
            # заканчиваем, если конец файла
            if not len_str1:
                break
            len_lastname = struct.unpack('i', len_str1)[0]
            lastname = f.read(len_lastname).decode('utf-8')
            
            len_str2 = f.read(4)
            len_name = struct.unpack('i', len_str2)[0]
            name = f.read(len_name).decode('utf-8')
            
            grade = struct.unpack('i', f.read(4))[0]
                        
            student += [lastname, name, grade]
            # расшифровываем в зависимости от сведений
            if grade == 1:
                mark = struct.unpack('i', f.read(4))[0]
                student.append(mark)
                student = first_grade_student(lastname, name, grade, mark)
            else:
                mark = round(struct.unpack('f', f.read(4))[0],2)
                if 2 <= grade <= 3:
                    student.append(mark)
                    student = second_or_third_grade_student(lastname, name, grade, mark)
                else:
                    student.append(mark)
                    student = fourth_grade_student(lastname, name, grade, mark)
            data.append(student)
        return data

print()
print("Обновленная база данных:")
print(f'{"Фамилия":<15} {"Имя":<12} {"Класс":<6} {"Скорость чтения":<20} {"К/Р по математике":<20} {"Итоговая аттестация":<20}')
print('-' * 100)

data = read_bin('3lab15.bin')
for student in data:
    print(student)
        