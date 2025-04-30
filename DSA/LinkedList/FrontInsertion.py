# Linked List with frond/ beginning of list insertion 

class Node():
    def __init__(self, data, next = None):        
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

# insert at beggining 
       
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
        

# List insersion at the end or if head is empty the return list 

    def insert_at_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(new_data, None)

# function to find length of linked list
    
    def get_length(self):
        count = 0
        itr = self.head 
        while itr:
            count +=1
            itr = itr.next 
        return count  
    
# function to remove specific node or element from linked list 
    def removeEle(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index passed for list')

        if index ==0:
            return self.head
        
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

# Insert at specific position in linked list or at given position
    def Insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Index Invalid')
        
        if index == 0:
            return self.insert_at_front(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next 



if __name__ == '__main__':
    list = LinkedList()
    list.insert_at_front(5)
    list.insert_at_front(6)
    list.insert_at_end(4)
    list.insert_at_end(3)
    list.print()
    list.Insert_at(7,8)
    list.print()
