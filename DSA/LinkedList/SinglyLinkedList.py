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
    
    def reverse_linked_list(self,head):

        curr = self.head
        prev = None

        while curr is not None:
            
            next_node = curr.next 

            curr.next = prev

            prev = curr
            curr = next_node

            print(prev)

        self.Rev_list = prev
        print(prev)
    

    def Print_rev(self):
        if self.head is None:
            print('List is Empty')
            return 

        itr = self.Rev_list
        rev_list = ''
        while itr:
            rev_list = str(itr.data) + ' -- '
            itr = itr.next

        print(rev_list)
    
    
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
    ll.inser_at_beggining(3)
    ll.inser_at_beggining(4)
    ll.inser_at_beggining(5)
    ll.print()
    ll.reverse_linked_list(1)
    ll.reverse_linked_list(2)
    ll.reverse_linked_list(3)
    ll.Print_rev()