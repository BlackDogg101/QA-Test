class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data): 
        new_node =  Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' => ' if current_node.next else '\n'
                  )
            current_node = current_node.next


linked_lst = LinkedList()
linked_lst.append(123)
linked_lst.append([1,2,3])
linked_lst.append("asd")
linked_lst.print_list()
linked_lst.prepend("nachalo")
linked_lst.print_list()
