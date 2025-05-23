"""
Для двух непустых двусвязных списков даны следующие объекты:
A1 и A2 — начало и конец первого списка, A0 — один из элементов второго списка.
Объединить исходные списки, поместив все элементы первого списка (в том же порядке)
после данного элемента второго списка, и вывести ссылки на первый и последний элементы
объединенного списка. Новые объекты типа Node не создавать.
"""

import numbers
import random


class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node


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

    def head_link(self) -> Node:
        if not self.is_empty():
            return self.head

    def tail_link(self) -> Node:
        if not self.is_empty():
            return self.tail

    def length(self) -> int:
        count: int = 0
        current: Node = self.head
        while current:
            count += 1
            current = current.next
        return count


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


def concatenate_lists(A1, A2, A0):
    """
    Объединяет два двусвязных списка, помещая все элементы первого списка перед элементом A0 второго списка.

    Args:
        A1: Начало первого списка.
        A2: Конец первого списка.
        A0: Элемент второго списка, перед которым нужно вставить первый список.

    Returns:
        first_node: Начало объединенного списка.
        last_node: Конец объединенного списка.
    """

    if A1 is None:  # Первый список пуст, ничего не делаем.
        return A0, find_last(A0)

    if A0 is None:  # Второй список начинается с null, значит A0 - некорректный элемент
        return A1, A2

    A1_last = A2  # Конец первого списка

    # Выводим данные элемента A0, перед которым вставляются элементы первого списка
    print(f"\nВставляем элементы первого списка перед элементом со значением: {A0.Data}")

    # Обновляем связи элементов
    if A0.Prev is not None:
        A0.Prev.next = A1  # Предыдущий элемент A0 теперь указывает на начало A1
    A1.Prev = A0.Prev  # Предыдущий для A1 - Предыдущий для A0
    A0.Prev = A2  # Предыдущий для A0 теперь A1_last
    A2.next = A0  # Последний элемент первого списка теперь указывает на A0

    #Определяем первый и последний элементы объединенного списка
    first_node = A1 if A1.Prev is None else find_first(A0)
    last_node = find_last(A0)

    return first_node, last_node


def find_last(node):
    """Находит последний элемент двусвязного списка, начиная с данного узла."""
    if not node:
        return None
    while node.Next:
        node = node.Next
    return node


def find_first(node):
    """Находит первый элемент двусвязного списка, начиная с данного узла."""
    if not node:
        return None
    while node.Prev:
        node = node.Prev
    return node


def create_random_doubly_linked_list(size, min_val=1, max_val=20):
    """Создает двусвязный список случайного размера со случайными значениями."""
    if size <= 0:
        return None, None

    head = Node(random.randint(min_val, max_val))
    tail = head
    for _ in range(size - 1):
        new_node = Node(random.randint(min_val, max_val), prev_node=tail)
        tail.next = new_node
        tail = new_node

    return head, tail


def main() -> None:
    # Создаем случайные списки
    size1 = random.randint(1, 5)  # Размер первого списка
    size2 = random.randint(1, 5)  # Размер второго списка

    A1, A2 = create_random_doubly_linked_list(size1)
    B1, B_last = create_random_doubly_linked_list(size2) # B_last нужен, чтобы не искать tail каждый раз

    # A0 - элемент второго списка, перед которым вставляем первый список.  Выбираем случайный элемент.
    A0 = B1
    if B1:
        current = B1
        for _ in range(random.randint(0, size2 - 1)): #random.randint(0, size2 - 1) генерирует случайный индекс для элемента A0
            if current.next:
                current = current.next
        A0 = current


    print("Первый список:")
    current = A1
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    print("Второй список:")
    current = B1
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    # Объединяем списки
    first_node, last_node = concatenate_lists(A1, A2, A0)

    print("\nОбъединенный список:")
    current = first_node
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    print("\nНачало объединенного списка:", first_node.data if first_node else "None")
    print("Конец объединенного списка:", last_node.data if last_node else "None")


if __name__ == "__main__":
    main()
