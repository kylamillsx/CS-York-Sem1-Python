from linkednode import LinkedNode
class LinkedQueue:
    def __innit__(self):
        self._front = None
        self._back = None
        self._size = 0
    def __str__(self):
        if self._front is None:
            return 'LinkedQueue([])'
        elements = []
        current = self._front
        while current is not None:
            elements.append(repr(elements.data))
            current = current.tail
        return 'LinkedQueue(['+ ','.join(elements)+'])'
    def enqueue(self, value):
        newnode = LinkedNode(value)
        if self._size == 0:
            self._front = newnode
            self._back = newnode
            #if its empty this new node is both front and back of queue
        else:
            #links the old back to the new node
            self._back.tail = newnode
            #makes the newnode the new back
            self._back = newnode
        self._size +=1
    def pop(self):
        if self._size==0:
            raise ValueError
        front = self._front #saving the front node to return it later
        self._front = self._front.tail #moves the front pointer forward
        #now we need to check if remvoing this made the queue empty
        if self._front is None:
            self._back = None #cuz if so front and back both are None
        front.tail = None #detaches the removed node
        self._size -= 1
        return front.data
    def peek(self):
        if self._size == 0:
            raise ValueError
        return self._front.data
    def __len__(self):
        return self._size 
    def isempty(self):
        if self._size == 0:
            return True
        else:
            return False
