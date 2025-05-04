class Hashmap():
    def __init__(self):
        self.size = 10 
        self.map = [[]for i in range(self.size)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)

        return h % 100
    
