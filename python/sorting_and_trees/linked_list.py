"""
This module will define a singly linked list class that will be able to be used to insert into a linked list,
delete from a linked list, search a linked list, and sort itnode.
"""

class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def search(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        
        while current.next is not None and current.next.value != value:
            current = current.next 
        
        if current.next == None:
            return False
        else:
            current.next = current.next.next
            return True

    def printer(self):
        current = self.head
        values = []

        while current is not None:
            values.append(current.value)
            current = current.next           
        return values

    def sort(self):
        sorted = False

        while not sorted:
            changed = False
            if self.head is None or self.head.next is None:
                sorted = True # Sorting one item
            if self.head.value > self.head.next.value:
                temp = self.head
                self.head = self.head.next
                temp.next = self.head.next
                self.head.next = temp
                changed = True
            current = self.head
            while current.next.next is not None:
                if current.next.value > current.next.next.value:
                    temp = current.next
                    current.next = current.next.next
                    temp.next = current.next.next
                    current.next.next = temp
                    changed = True
                current = current.next
                
            if not changed:
                sorted = True

            
            

class Node:
    def __init__(node, value):
        node.value = value
        node.next = None
