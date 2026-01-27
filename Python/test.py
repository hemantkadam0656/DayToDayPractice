class NestedList:
    def __init__(self, ns):
        self.stack = ns[::-1]

    def next(self):
        return self.stack.pop().get


if __name__ == '__main__':
    NS = [ [1,1], 2, [1,1] ]
    res = NestedList(NS)
