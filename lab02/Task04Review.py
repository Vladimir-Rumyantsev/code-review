"""
Дан односвязный линейный список и указатель на голову списка P1.
Необходимо вставить значение M после каждого третьего элемента списка,
и вывести ссылку на последний элемент полученного списка P2.
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


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        line: str = ''
        current: Node = self.head
        while current:
            line += f", {current}"
            current = current.next
        return f"[{line[2:]}]"

    def is_empty(self) -> bool:
        return self.head is None

    def length(self) -> int:
        count: int = 0
        current: Node = self.head
        while current:
            count += 1
            current = current.next
        return count

    def str_tail_link(self) -> str:
        if self.is_empty():
            return "The queue is empty."
        current: Node = self.head
        while current.next:
            current = current.next
        return current.str_link()

    def add(self, data, index: int = -1) -> None:
        new_node = Node(data)
        length: int = self.length()
        if index < 0:
            index += (length + 1)
        if index < 0 or index > length:
            raise IndexError("Index out of range.")

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current: Node = self.head
        for _ in range(index-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node


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


def main() -> None:
    linked_list: LinkedList = LinkedList()
    list_size: int = input_number(
        prompt="\nВведите количество элементов для листа (не больше 10): ",
        min_val=0,
        max_val=10,
        data_type=int
    )
    for i in range(list_size):
        data: str = input(f"Введите элемент {i+1} для листа: ")
        linked_list.add(data=data)
    data: str = input(f"\nВведите значение M для вставки после каждого третьего элемента: ")

    print(
        f"\nЛист до преобразований: {linked_list}"
        f"\nСсылка на последний элемент: {linked_list.str_tail_link()}"
    )

    m_insertion_count: int = (list_size // 3)
    index: int = -1
    for _ in range(m_insertion_count):
        index += 4
        linked_list.add(data=data, index=index)
    print(
        f"\nЛист после вставок M:   {linked_list}"
        f"\nСсылка на последний элемент: {linked_list.str_tail_link()}"
    )


if __name__ == "__main__":
    main()
