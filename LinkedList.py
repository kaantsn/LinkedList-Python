class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Bağlı liste oluştur
linked_list = LinkedList()

# Elemanlar ekleyelim
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Bağlı listeyi yazdıralım
linked_list.display()
