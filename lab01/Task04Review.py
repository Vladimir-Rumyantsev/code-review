"""
программа считывает данные об N учениках и записывает их в бинарный файл
ввод: N (число записей), затем сведения об N учениках (Фамилия, Имя, Класс, Скорость чтения (int, 1 кл.) /
Баллы за контрольную по математике (от 1 до 10, float, 2-3 кл.) /
Баллы за итоговую аттестацию (от 1 до 100, float, 4 кл.))
вывод: содержимое файла в виде таблицы
"""

import numbers
import struct


class Student:
    def __init__(self, lastname: str, name: str, grade: int) -> None:
        self.lastname = lastname
        self.name = name
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.lastname:<15} {self.name:<12} {self.grade:<6}"


class FirstGradeStudent(Student):
    def __init__(self, lastname: str, name: str, grade: int, mark: int) -> None:

        if grade != 1:
            raise ValueError("Grade must be 1 for FirstGradeStudent.")

        super().__init__(lastname=lastname, name=name, grade=grade)
        self.mark = mark

    def __str__(self) -> str:
        return (
            super().__str__()
            + f" {self.mark:<20} {'-':<20} {'-':<20}"
        )


class SecondOrThirdGradeStudent(Student):
    def __init__(self, lastname: str, name: str, grade: int, mark: float) -> None:

        if grade not in [2, 3]:
            raise ValueError("Grade must be 2 or 3 for SecondOrThirdGradeStudent.")

        super().__init__(lastname=lastname, name=name, grade=grade)
        self.mark = mark

    def __str__(self) -> str:
        return (
            super().__str__()
            + f" {'-':<20} {self.mark:<20} {'-':<20}"
        )


class FourthGradeStudent(Student):
    def __init__(self, lastname: str, name: str, grade: int, mark: float) -> None:

        if grade != 4:
            raise ValueError("Grade must be 4 for FourthGradeStudent.")

        super().__init__(lastname=lastname, name=name, grade=grade)
        self.mark = mark

    def __str__(self) -> str:
        return (
            super().__str__()
            + f" {'-':<20} {'-':<20} {self.mark:<20}"
        )


def input_number(
        prompt: str = "Введите число: ",
        min_val: numbers = 0,
        max_val: numbers = float("inf"),
        data_type: numbers = int
) -> numbers:
    while True:
        try:
            value = data_type(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Error: Value must be between {min_val} and {max_val}")
        except ValueError:
            print("Error: Invalid input. Expected number.")


def input_student():
    lastname = input("Фамилия: ")
    name = input("Имя: ")
    grade = input_number(
        prompt="Класс (1-4): ",
        min_val=1,
        max_val=4,
        data_type=int
    )

    if grade == 1:
        mark = input_number(
            prompt="Скорость чтения (кол-во слов/мин): ",
            min_val=0,
            max_val=float("inf"),
            data_type=int
        )
        return FirstGradeStudent(lastname, name, grade, mark)

    elif 2 <= grade <= 3:
        mark = input_number(
            prompt="Оценка от 1 до 10 за итоговую школьную аттестацию: ",
            min_val=1,
            max_val=10,
            data_type=float
        )
        return SecondOrThirdGradeStudent(lastname, name, grade, mark)

    elif grade == 4:
        mark = input_number(
            prompt="Баллы от 1 до 100 за итоговую аттестацию: ",
            min_val=1,
            max_val=100,
            data_type=float
        )
        return FourthGradeStudent(lastname, name, grade, mark)


def write_bin(file_path: str, data: list):
    with open(file_path, "ab") as f:
        for student in data:
            lastname_encoded = student.lastname.encode("utf-8")
            f.write(struct.pack('i', len(lastname_encoded)))
            f.write(lastname_encoded)

            name_encoded = student.name.encode("utf-8")
            f.write(struct.pack('i', len(name_encoded)))
            f.write(name_encoded)

            f.write(struct.pack('i', student.grade))

            if isinstance(student, FirstGradeStudent):
                f.write(struct.pack('i', student.mark))
            else:
                f.write(struct.pack('f', student.mark))


def read_bin(file: str) -> list:
    with open(file, "rb") as f:
        data = []
        while True:
            len_lastname = f.read(4)
            if not len_lastname:
                break

            lastname = f.read(
                struct.unpack('i', len_lastname)[0]
            ).decode("utf-8")

            name = f.read(
                struct.unpack('i', f.read(4))[0]
            ).decode("utf-8")

            grade = struct.unpack('i', f.read(4))[0]

            if grade == 1:
                mark = struct.unpack('i', f.read(4))[0]
                student = FirstGradeStudent(lastname, name, grade, mark)
            else:
                mark = round(struct.unpack('f', f.read(4))[0], 2)
                if 2 <= grade <= 3:
                    student = SecondOrThirdGradeStudent(lastname, name, grade, mark)
                else:
                    student = FourthGradeStudent(lastname, name, grade, mark)
            data.append(student)
        return data


def main():
    students = []
    num_students = input_number(
        prompt="Введите число студентов для добавления: ",
        min_val=1,
        max_val=float("inf"),
        data_type=int
    )

    for _ in range(num_students):
        print()
        student = input_student()
        students.append(student)

    write_bin(file_path="3lab15.bin", data=students)

    header = (
        f"{'Фамилия':<15} {'Имя':<12} {'Класс':<6} {'Скорость чтения':<20} "
        f"{'К/Р по математике':<20} {'Итоговая аттестация':<20}"
    )
    print(f"\nОбновленная база данных:\n" + header)
    print("-" * 100)

    data = read_bin(file="3lab15.bin")
    for student in data:
        print(student)


if __name__ == "__main__":
    main()
