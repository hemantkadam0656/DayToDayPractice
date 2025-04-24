class Node():
    def __init__(self, new_data, next = None):
        self.data = new_data
        self.next = next
        
class linkedlist():
    def __init__(self):
        self.head = None
    
    def insert_at_front(self, data):
        n_node = Node(data, self.head)
        self.head = n_node
    
    def print(self):
        if self.head is None:
            print('list is empty')
            return 
        
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + ' --> '
            itr = itr.next
        
        print(llist)

if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_at_front(5)
    ll.insert_at_front(6)
    ll.insert_at_front(7)
    ll.print()