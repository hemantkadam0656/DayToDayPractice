class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    

class linkedList():
    def __init__(self):
        self.head = None
    
    def inser_at_beggining(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def print(self):
        if self.head is None:
            print('List is Empty')
            return 
        
        itr = self.head
        list = ''
        while itr:
            list += str(itr.data) + ' -- '
            itr = itr.next
        
        print(list + 'None')


if __name__ == '__main__':
    ll = linkedList()
    ll.inser_at_beggining(1)
    ll.inser_at_beggining(2)
    ll.print()