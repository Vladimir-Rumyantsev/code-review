#ListWork8. Дан односвязный линейный список и указатель на голову списка P1. Необходимо
#вывести указатель на девятый элемент этого списка P9. Известно, что в исходном списке не
#менее 9 элементов.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_h(self, data): #Добавить в head
        if self.head == None:
            self.head = Node(data)
            self.tail = Node(data)
            return
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    def add_t(self, data): #Добавить в tail
        if self.head == None:
            self.head = Node(data)
            self.tail = Node(data)
            return
        else:
            newnode=Node(data)
            selfnode = self.head
            while selfnode.next is not None:
                selfnode = selfnode.next
            selfnode.next = newnode
            self.tail=newnode
    def delete_t(self): #удалить tail
        if self.head == None:
            return
        else:
            newnode = self.head
            while newnode.next.next is not None:
                newnode=newnode.next
            self.tail=newnode
            newnode.next = None
    def delete_h(self): #удалить head
        if self.head == None:
            return
        else:
            newnode = self.head
            self.head=newnode.next

    def display(self): #отображение
        iternode = self.head
        if self.head==None:
            print("Stack Underflow")
        else:
            while (iternode != None):
                print(iternode.data, end="")
                iternode = iternode.next
                if (iternode != None):
                    print(" -> ", end="")
            return
    def find_nom(self): #Поиск
        iternode = self.head
        if self.head==None:
            print("Stack Underflow")
        else:
            count=1
            while (iternode != None) and count !=9:
                iternode = iternode.next
                count+=1
            print(iternode)
            return iternode.data

a=List()
k=1
for i in range(12):
    a.add_t(k)
    k+=1

a.display()
print("")
a.find_nom()
#print(a.find_nom()) #для того чтобы показать, что выводим нужное число