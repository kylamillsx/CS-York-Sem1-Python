class Rectangle:

    def __init__(self, coordX=0, CoordY=0, width=1, length=1):
        if width <=0 or length <= 0:
            raise ValueError('Invalid Inputs!')
        self.x = coordX
        self.y = CoordY
        self._w = width
        self._l = length

    def area(self):
        return self._w * self._l
    
    #getters   
    @property 
    def width(self):
        return self._w
    
    @property
    def length(self):
        return self._l
    
    #setters      
    @width.setter  
    def width(self, w):
        if w <= 0:
            raise ValueError('Invalid input!')
        self._w = w
        
    @length.setter
    def length(self, l):
        if l<= 0:
            raise ValueError('Invalid input!')
        self._l = l
        
        
        
        
    
    
