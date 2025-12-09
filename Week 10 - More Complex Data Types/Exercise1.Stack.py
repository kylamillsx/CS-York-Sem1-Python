from linkednode import LinkedNode
class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    #adds value to top of stack
    def push(self, value):
        newnode = LinkedNode(value)#makes new node holding the value 
        newnode.tail = self._top#link the new node to current top 
        self._top = newnode#updates top of stack to be new node
        self._size +=1

    def __str__(self):
        if self._top is None:#no nodes means an empty stack
            return 'Linked List[]'
        elements = []#empty list will hold all values from top to bottom
        current = self._top#starts at top node
        while current is not None:#traverse till end of stack is reached
            elements.append(repr(current.data))#add node data to list
        return 'LinkedStack(['+','.join(elements)+'])'#outputs it all
    
    def pop(self):
        if self._size == 0:
            raise ValueError#cuz it cant pop from empty stack
        top_node = self._top#storing current top nodes value so we can return it later
        self._top = self._top.tail#moves top pointer to next node down
        top_node.tail = None #like the old top node never existed
        self._size -=1 
        return top_node.data#returns data stored in old top node
    
    def peek(self):
        if self._size == 0:
            raise ValueError
        return self._top.data #returns data stored in top node
    
    def __len__(self):
        return self._size 
    def isempty(self):
        if self._size == 0:
            return True
        else:
            return False
    
