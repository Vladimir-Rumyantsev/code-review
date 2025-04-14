"""
ListWork8. Дан односвязный линейный список и указатель на голову списка P1.
Необходимо вывести указатель на девятый элемент этого списка P9.
Известно, что в исходном списке не менее 9 элементов.
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
        self.tail = None

    def __str__(self) -> str:
        line: str = ''
        current: Node = self.head
        while current:
            line += f", {current}"
            current = current.next
        return f"[{line[2:]}]"

    def is_empty(self) -> bool:
        return self.head is None

    def str_head_link(self) -> str:
        if self.is_empty():
            return "The queue is empty."
        return self.head.str_link()

    def str_tail_link(self) -> str:
        if self.is_empty():
            return "The queue is empty."
        return self.tail.str_link()

    def push(self, data: object) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add(self, data: object) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def length(self) -> int:
        count: int = 0
        current: Node = self.head
        while current:
            count += 1
            current = current.next
        return count

    def pop(self, index: int = -1) -> object:
        length: int = self.length()
        if index < 0:
            index += length
        if index < 0 or index >= length:
            raise IndexError("Index out of range.")

        current: Node = self.head

        if length == 1:
            self.head = None
            self.tail = None
            return current.data

        if index == 0:
            self.head = current.next
            return current.data

        for _ in range(index - 1):
            current = current.next

        if index == length - 1:
            self.tail = current

        data: object = current.next.data
        current.next = current.next.next
        return data

    def get_node_at(self, index: int = -1) -> Node:

        length: int = self.length()
        if index < 0:
            index += length
        if index < 0 or index >= length:
            raise IndexError("Index out of range.")

        if index == length - 1:
            return self.tail

        current: Node = self.head
        for _ in range(index):
            current = current.next
        return current


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
    linked_list = LinkedList()
    list_size = input_number(
        prompt="\nВведите количество элементов для листа (не больше 20): ",
        min_val=0,
        max_val=20,
        data_type=int
    )
    for i in range(list_size):
        data = input(f"Введите элемент {i+1} для листа: ")
        linked_list.add(data=data)

    try:
        ninth_node: Node = linked_list.get_node_at(index=8)
        print(
            f"\nЛист: {linked_list}"
            f"\nДевятый элемент: {ninth_node}"
            f"\nСсылка на девятый элемент: {ninth_node.str_link()}"
        )
    except IndexError as ex:
        print(
            f"\nЛист: {linked_list}"
            f"\n\nВо время поиска девятого элемента произошла ошибка.\n{ex}"
        )


if __name__ == "__main__":
    main()
