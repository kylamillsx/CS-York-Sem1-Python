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







