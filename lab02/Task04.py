# Дан односвязный линейный список и указатель на голову списка P1. Необходимо
#  вставить значение M после каждого третьего элемента списка, и вывести ссылку на последний
#  элемент полученного списка P2
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
class Queue:
    def __init__(self):
        self.head = None
    def push(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
    def printqueue(self):
        current = self.head
        while current is not None:
            print(current, end=' ')
            current = current.next
        print()

ONE = Queue()
for i in [3, 4, 7, 9, 7, 8]:
    ONE.push(i)

P1 = ONE.head
M = input('Введите M -> ')
try:
    M = int(M)
except ValueError:
    print("M должно быть целым числом")
    exit()

print('Изначальный список: ', end='')
ONE.printqueue()

count = 0
while P1 is not None:
    count += 1
    if count % 3 == 0:
        m = Node(M)
        m.next = P1.next
        P1.next = m
        P1 = m
    P1 = P1.next

print('Итоговый список: ', end='')
ONE.printqueue()

P2 = ONE.head
while P2 is not None and P2.next is not None:
    P2 = P2.next

print(f'Значение последнего элемента: {P2.data}')
print(f'Ссылка на последний элемент: {ONE}')