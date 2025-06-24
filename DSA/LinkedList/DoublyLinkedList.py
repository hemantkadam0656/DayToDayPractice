# doubly linked list node 
class Node:
    def __init__(self,data, prev = None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# class declared for doubly linked list 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # print linked list
    def print_forward(self):
        if self.head is None:
            print('List is empty')
        
        itr = self.head
        list = ''
        while itr:
            list += str(itr.data) + ' --> '
            itr = itr.next
        
        print(list + 'None')

    # Print reverse linked list 
    def print_backword(self):
        if self.head is None:
            print('List is empty')
        
        last_node = self.get_last_node()
        itr = last_node
        list = ''
        while itr:
            list += str(itr.data) + ' --> '
            itr = itr.prev

        print(list + 'None')
    
    # insert at first postion/ Beginning of list 
    def insert_at_begining(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node

        else:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node

    # to get last node of list 
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        
        return itr 

    # find the length of doubly linked list  
    def get_length(self):
        if self.head is None:
            print('Linked List is empty')
        
        else:
            itr = self.head
            count = 0
            while itr:
                count += 1
                itr = itr.next

        print('Length of linked List :- ', count)
        return count 

    # insert at end of list 
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data,None,None)
            self.head = node
            return self.head

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, itr, None)


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_at_begining(3)
    ll.insert_at_begining(4)
    ll.print_forward()
    ll.get_length()
    ll.insert_at_end(12)
    ll.print_forward()