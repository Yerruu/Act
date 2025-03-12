class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class List:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return  
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print1 (self,node):
        if node is None:
            return
        print(node.data)
        self.print1(node.next)
                   
    def start(self):
        self.print1(self.head)

list = List()

list.insert(1)
list.insert(331)
list.insert(21)
list.insert(121)

print("The list is:")
list.start()



