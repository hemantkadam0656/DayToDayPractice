class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class FrondInsertion():
    def __init__(self):
        self.head = None

    def newinsertion(self,data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def print(self):
        if self.head is None:
            return

        itr = self.head
        llist= ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next

        print(llist + 'None') 

# main function 
# def main():
obj =  FrondInsertion()
obj.newinsertion(5)
obj.newinsertion(6)
obj.print()  

# if __name__ == '__main__':
#     main()