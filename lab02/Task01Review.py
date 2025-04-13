"""
Дано число D и вершина A1 непустого стека. Добавить элемент со значением D в
стек и вывести ссылку A2 на новую вершину стека.
"""


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

    def str_link(self) -> str:
        return super().__str__()


class Stack:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, data) -> None:
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("Error: The stack is empty!")

        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data

    def peek(self) -> object:
        if self.is_empty():
            return None
        return self.head.data

    def str_head_link(self) -> str:
        if self.is_empty():
            return "The stack is empty."
        return self.head.str_link()

    def __str__(self) -> str:
        line = ''
        current = self.head
        while current:
            line += f", {current}"
            current = current.next
        return f"[{line[2:]}]"


def main() -> None:
    stack = Stack()
    stack.push(data=100)
    A1: str = stack.str_head_link()

    while True:
        try:
            D = int(input("\nВведите число D: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    stack.push(data=D)
    A2: str = stack.str_head_link()

    print(
        f"\nИсходная ссылка на вершину стека:    {A1}"
        f"\nОбновлённая ссылка на вершину стека: {A2}"
        f"\n\nСтек: {stack}"
    )


if __name__ == "__main__":
    main()
