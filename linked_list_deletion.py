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
            print(temp.value, end = " ")
            temp = temp.next

    def insert_node(self, insert_value):
        temp = Node(insert_value)
        if(self.head == None):
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp            


    def delete_node(self, del_value):
        current = self.head    #current
        prev = None

        if(current == None):
            print("Empty Linked List")
            return

        while(current):
            if(current.value == del_value):
                break
            prev = current
            current = current.next

        if(current == None):
            print("No node found with value " + del_value)
            return


        prev.next = current.next
        current = None       
        


ll = linked_list()

ll.insert_node("Node1")
ll.insert_node("Node2")
ll.insert_node("Node3")
ll.insert_node("Node4")
ll.insert_node("Node5")

ll.print_list()
print()

ll.delete_node("Node3")
ll.print_list()

# print()
# emptyList = linked_list()
# emptyList.delete_node("Node1")





