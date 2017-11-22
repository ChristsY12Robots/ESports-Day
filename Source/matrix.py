
# in development 22/11/17 Nathan
"""
Simple Vector/Matrix program.

Note:
    All functions that by nature do not return a value, will return 1 if an error occurs. No error message is displayed when something goes wrong.
    Similarly zero is returned if there is no error.

Vector:
    Vectors can be used for coordinates.

    __init__(n): n is the size of the vectors. a vectors of size n has n elements.
    
    update_comp(index , value): updates the component at "index" of the vector to "value"
    update_vec(list_data): list data is a list of numbers. if the the length of "list_data" is the same as the size of the vector, then the whole
        vector if updated to the "list_data"

Matrix:

    A matrix class is implemented as a list of vectors. This is useful for polygons/shapes that have many vertices. Each vertex is a vector in the matrix.

"""

class Vector():
    def __init__(self , n):
        self.size = n
        self.vec = []
        for i in range(0 , n , 1): # create a vector of size n
            self.vec.append(0)

    def update_comp(self , index , value):
        if (index >= self.size): # "out of range" check.
            return (1)
        self.vec[index] = value

    def update_vec(self , list_data):
        if (len(list_data) != self.size): # the list "list_data" has to be the same size to the size of the vector.
            return (1)

        for i in range(0 , self.size , 1):
                self.vec[i] = list_data[i]
        
            
    def print_vec(self):
        print ("{" , end = "")
        for i in range(0 , self.size , 1):
            if (i == self.size-1): # if i is at the last element.
                print (str(self.vec[i]) + "}" , end = "")# this will prevent a comma at the end of printing.
                return (1) #the printout would look like as follows without the if statement: |1 , 5 , 3  ,| . notice the comma at the end.
            print (str(self.vec[i]) + " , " , end = "")


class Matrix():
    def __init__(self , rows_in , columns_in):
        self.rows = rows_in
        self.columns = columns_in

        self.data = [] # this is the data that stores the matrix.

        for i in range(0 , columns_in , 1): # create the matric structure from a list of vectors.
            self.data.append(Vector(rows_in))

    def update_comp(self , column_in , row_in , value):
        if (column_in >= self.columns): # checking for "out of range". rows are checked by the vectors.
            return (1)

        self.data[column_in].update_comp(row_in , value)

    def update_vector(self , index , list_data):
        if (index >= self.columns): # checking to see if "index" is out of range.
            return (1)
        self.data[index].update_vec(list_data)

    def update_matrix(self , copy): # copy has to be a list of vectors.
        if (len(copy) != self.columns): # copy has to have the same amount of columns. if not, return is called.
            return (1)
        for i in range(0 , self.columns , 1): # if any of the elements in copy is not a vector, return is called.
            if (isinstance(copy[i] , Vector) == False):
                return (1)
        self.data = copy # it is now safe to copy the data.
        
        
    def print_matrix(self):
        print ("{" , end = "")
        for i in range(0 , self.columns , 1):
            if (i == self.columns-1):
                self.data[i].print_vec()
                print ("}")
                return
            self.data[i].print_vec()
            print (" , " , end = "")


mat = Matrix(3 , 4)
mat.update_comp(2 , 2 , 1)
mat.print_matrix()
