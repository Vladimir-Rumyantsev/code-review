"""
Дано число D и вершина A1 непустого стека. Добавить элемент со значением D в
стек и вывести ссылку A2 на новую вершину стека.
"""

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.is_empty():
            print("Ошибка: Стек пуст!")
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

def main():
    stack = Stack()
    stack.push(100) #A1
    print("Исходна вершина стека A1:", stack.head) # Вывод ссылки на узел A1

    while True:
        try:
            D = float(input("Введите число D: "))
            break
        except ValueError:
            print("Ошибка! Повторная попытка...")
            continue

    # Добавление элемента D в стек
    stack.push(D)

    A2 = stack.head
    print("Новая вершина стека A2:", A2)

if __name__ == '__main__':
    main()