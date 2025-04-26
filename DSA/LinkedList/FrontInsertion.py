# Linked List with frond/ beginning of list insertion 

class Node():
    def __init__(self, data, next = None):        
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        
    def insert_at_front(self, new_data):
        new_node = Node(new_data, self.head)
        self.head = new_node
    
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return 
        
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + ' --> '
            itr = itr.next   

        print(llist + 'None')


    def insert_at_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(new_data, None)
    
        

if __name__ == '__main__':
    list = LinkedList()
    list.insert_at_front(5)
    list.insert_at_front(6)
    list.insert_at_end(4)
    list.insert_at_end(3)
    list.print()
