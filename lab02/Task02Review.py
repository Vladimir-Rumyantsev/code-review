"""
Даны две очереди; начало и конец первой равны A1 и A2, а второй — A3 и A4
(если очередь является пустой, то соответствующие объекты равны null).
Переместить все элементы первой очереди (в порядке от начала к концу) в конец второй очереди
и вывести ссылки на начало и конец преобразованной второй очереди.
Новые объекты типа Node не создавать.
"""

import numbers


class Node:
    def __init__(self, data: object, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

    def str_link(self) -> str:
        return super().__str__()


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        return self.head is None

    def add(self, data: object) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("Error: The queue is empty!")

        removed_node = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return removed_node.data

    def extend(self, queue: 'Queue') -> None:
        if queue.is_empty():
            return

        if self.is_empty():
            self.head = queue.head
        else:
            self.tail.next = queue.head
        self.tail = queue.tail
        queue.head = None
        queue.tail = None

    def str_head_link(self) -> str:
        if self.is_empty():
            return "The queue is empty."
        return self.head.str_link()

    def str_tail_link(self) -> str:
        if self.is_empty():
            return "The queue is empty."
        return self.tail.str_link()

    def __str__(self) -> str:
        line = ''
        current = self.head
        while current:
            line += f", {current}"
            current = current.next
        return f"[{line[2:]}]"


def input_number(
        prompt: str = "Введите число: ",
        min_val: numbers = 0,
        max_val: numbers = float("inf"),
        data_type: type = int
) -> numbers:
    while True:
        try:
            value = data_type(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Error: Value must be between {min_val} and {max_val}")
        except ValueError:
            print("Error: Invalid input. Expected number.")


def main():
    queue1 = Queue()
    queue2 = Queue()

    queue1_size = input_number(
        prompt="\nВведите количество элементов для первой очереди (не больше 10): ",
        min_val=0,
        max_val=10,
        data_type=int
    )
    for i in range(queue1_size):
        data = input(f"Введите элемент {i+1} для первой очереди: ")
        queue1.add(data=data)

    queue2_size = input_number(
        prompt="\nВведите количество элементов для второй очереди (не больше 10): ",
        min_val=0,
        max_val=10,
        data_type=int
    )
    for i in range(queue2_size):
        data = input(f"Введите элемент {i+1} для второй очереди: ")
        queue2.add(data=data)

    print(
        f"\nПервая очередь до перемещения: {queue1}"
        f"\nВторая очередь до перемещения: {queue2}"
    )

    queue2.extend(queue1)

    print(
        f"\nПервая очередь после перемещения: {queue1}"
        f"\nВторая очередь после перемещения: {queue2}\n"
        f"\nСсылка на начало второй очереди: {queue2.str_head_link()}"
        f"\nСсылка на конец второй очереди:  {queue2.str_tail_link()}"
    )


if __name__ == "__main__":
    main()
