#Даны две очереди; начало и конец первой равны A1 и A2, а второй — A3 и A4(если очередь является пустой,
#то соответствующие объекты равны null). Переместить все элементы первой очереди (в порядке от начала к концу)в конец
#второй очереди и вывести ссылки на начало и конец преобразованной второй очереди. Новые объекты типа Node не создавать.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self): # Проверка на пустую очередь
        return self.head is None

    def enqueue(self, data): # Добавление элемента в конец очереди
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self): # Удаление из начала очереди
        if self.is_empty():
            raise IndexError("Очередь пуста")

        removed_node = self.head
        self.head = self.head.next  # Перемещаем указатель head на следующий узел

        if self.head is None:
            self.tail = None

        return removed_node.data

    def print_queue(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Создаем две очереди
queue1 = Queue()
queue2 = Queue()

num_elements1 = int(input("Введите количество элементов для первой очереди: "))
for i in range(num_elements1):
    data = input(f"Введите элемент {i+1} для первой очереди: ")
    queue1.enqueue(data)

num_elements2 = int(input("Введите количество элементов для второй очереди: "))
for i in range(num_elements2):
    data = input(f"Введите элемент {i+1} для второй очереди: ")
    queue2.enqueue(data)

print("Первая очередь до перемещения:")
queue1.print_queue()
print("Вторая очередь до перемещения:")
queue2.print_queue()

# начало и конец первой очереди
A1 = queue1.head
A2 = queue1.tail
# начало и конец второй очереди
A3 = queue2.head
A4 = queue2.tail

# Перемещаем элементы из первой очереди во вторую
if not queue1.is_empty():
    if queue2.is_empty():
        queue2.head = A1
        queue2.tail = A2
    else: # Если вторая очередь не пуста
        A4.next = A1
        queue2.tail = A2
    queue1.head = None
    queue1.tail = None
else:
    print("Первая очередь пуста, перемещать нечего")

print("Вторая очередь после перемещения:")
queue2.print_queue()
if queue2.head:
    print("Новое начало второй очереди:", queue2.head.data)
    print("Ссылка на начало второй очереди:", queue2.head)
else:
    print("Вторая очередь пуста")
if queue2.tail:
    print("Новый конец второй очереди:", queue2.tail.data)
    print("Ссылка на конец второй очереди:",queue2.tail)
else:
    print("Вторая очередь пуста")