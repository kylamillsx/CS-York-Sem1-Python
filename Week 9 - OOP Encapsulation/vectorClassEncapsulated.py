class Vector:
    def __init__(self,data=None):
        if data is None:
            self._vector = []
        else:
            self._vector = data.copy()

    def __str__(self):
        if self._vector == None:
            return "<>"
        else:
            s = str(self._vector).strip("[]").replace(" ","")
            return "<"+s+">"
    def __eq__(self, other_vector):#compares two vectors, equals method
        if not isinstance(other_vector, Vector):
            return False
        if self.dim() != other_vector.dim():
            return False
        for i in range(len(self._vector)):
            if self._vector[i] != other_vector._vector[i]:
                return False
        return True
    def __ne__(self, other_vector):#not equals too 
        return not self.__eq__(other_vector)
    
    #addition of vectors
    def __add__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError
        if self.dim() != other_vector.dim():
            raise ValueError
        resultList = [self._vector[i] + other_vector._vector[i] for i in range(self.dim())]
        return Vector(resultList)
    
    #scalar multiplication from right side
    def __rmul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError
        else:
            resultList = [i * scalar for i in self._vector]
            return Vector(resultList)
    
    #scalar multiplication
    def __mul__(self, scalar):
        raise TypeError#cuz u cant do vector * scalar only scalar * vector
    
    #in place addition
    def __iadd__(self, other_vector):
        if not isinstance(other_vector, Vector):#checking if other is a vector 
            raise TypeError
        if (self.dim()) != (other_vector.dim()) :#checking if dimensions are the same
            raise ValueError
        for i in range((self.dim())):#self.dim means dimension aka all values
            self._vector[i] += other_vector._vector[i]
        return self
    
    #in place multiplication
    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError
        for i in range(self.dim()):
            self._vector[i] *= scalar
        return self
    
    #getter method
    def get(self, index):
        return self._vector[index]
    #setter method
    def set(self,index,value):
        self._vector[index] = value
    #scalar product
    def scalar_product(self,scalar):
        resultList = [i * scalar for i in self._vector]#adds scalar times each element within list of vector to a new list
        return Vector(resultList)#adding that list to the new vector 
    #dimension
    def dim(self):#returns dimension aka number elements in vector
        if self._vector == None:
            return 0
        else:
            return len(self._vector)
    #addition of vectors
    def add(self, other_vector):
        if not isinstance(other_vector, Vector):#checks if its instance of Class Vector
            raise TypeError
        else:
            if other_vector.dim() != self.dim():
                raise ValueError
            else:
                a = self._vector[0] + other_vector._vector[0]
                b = self._vector[1] + other_vector._vector[1]
                c = self._vector[2] + other_vector._vector[2]
                addedVector = Vector([a,b,c])
                return addedVector
    #checking they have equivalent values
    def equals(self,other_vector):
        if isinstance(other_vector, Vector):
            if self.dim() != other_vector.dim():
                return False
            else:
                for i in range (len(self._vector)):
                    if self._vector[i] != other_vector._vector[i]:
                        return False
                return True
        else:
            return False

vector1 = Vector([1,2,3])
vector2 = Vector([1,2,3])







