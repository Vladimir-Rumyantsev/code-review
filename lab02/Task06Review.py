# Dynamic79
# даны ссылки на барьерный и текущий элементы двусвязного списка
# Описать класс IntListB:
# закрытые поля barrier и current типа Node
# конструктор с параметрами aBarrier и aCurrent
# процедура InsertLast(D), которая добавляет элемент D в конец списка (добавленный элемент становится текущим)
# процедура Put(), которая выводит ссылку на поле current
# процедура ToLast (делает текущим последний элемент списка)
# процедура ToPrev (делает текущим предыдущий элемент в списке)
# функция GetData целого типа (возвращает значение текущего элемента списка)
# функция IsBarrier (возвращает true, если текущий элемент списка - барьер, и false в противном случае)

# вывести все четные значения элементов исходного списка, просматривая список с конца
# вывести также количество элементов в списке (барьерный элемент не считается)

import random

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return str(self.data)
    
class IntListB:
    def __init__(self, aBarrier, aCurrent=None):
        self.barrier = aBarrier 
        self.current = aCurrent  
    
    def InsertLast(self, D): # вставка эл-та D в конец списка
        new_node = Node(D)
        new_node.prev = self.barrier.prev
        new_node.next = self.barrier
        self.barrier.prev.next = new_node
        self.barrier.prev = new_node
        self.current = new_node
    
    def Put(self):
        return f'Ссылка на текуший элемент списка: {self.current}'
    
    def ToLast(self):
        if self.barrier.prev != self.barrier:
            self.current = self.barrier.prev
        
    def ToPrev(self):
        if self.barrier.next != self.barrier:
            self.current = self.current.prev
                
    def GetData(self):
        return int(self.current.data)
    
    def IsBarrier(self):
        return self.current == self.barrier
                
    def Print(self):
        current = self.barrier.next
        while current != self.barrier: # вывожу весь список, пока не дойду до барьера
            print(str(current.data), end=', ')
            current = current.next
        print()       
    
# создаем барьер и список
barrier = Node(0)
barrier.next = barrier
barrier.prev = barrier
list = IntListB(barrier, barrier)
elems = [random.randint(1,50) for _ in range(random.randint(10,20))]
for elem in elems:
    list.InsertLast(elem)

    
print('Исходный список:')
list.Print()
print(list.Put())

list.ToLast()
count = 0
cur = list.current
print('Четные элементы списка:')
while not list.IsBarrier():
    data = list.GetData()
    if data % 2 == 0:
        print(data, end=', ')
    count += 1
    list.ToPrev()
print()
print(f'Количество элементов в списке: {count}')