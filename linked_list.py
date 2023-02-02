class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next


ll = linked_list()

ll.head = Node("Node1")
# ll.tail = ll.head

second = Node("Node2")
third = Node("Node3")

ll.head.next = second

second.next = third
ll.tail = third


ll.print_list()





