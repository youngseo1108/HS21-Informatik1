'''
# TASK 4. Matrix
build a class Matrix with basic capabilities of multiplication and addition 
to illustrate these steps usually just abstracted away by a calculator.

- Constructor: An instance of Matrix should be created via a nested list, ie. M = Matrix([[1,1], [1,1]])
- Each list embedded in the larger list corresponds to one row in the matrix
- The indices within the embedded lists correspond to the columns.
- If the constructor input satisfies the following properties it should be stored as a private instance variable:
1. It contains exactly 2 dimensions, the input to the constructor is a list of lists of either integers or floats.
2. The nested lists passed to the constructor form an exact rectangle, meaning all rows are of the exact same length.
3. The nested lists passed to the constructor may not be empty [[]].
- If the above conditions are not satisfied, an AssertionError should be thrown 
(you may use the assert x == y, "error message in case of assertion failure" syntax).
- make sure that two instancesA and B of class Matrix can be added via the + operator, 
i.e. C = A + B should work To do this, implement __add__(self, other) and return a new Matrix instance.
- make sure that two instancesA and B of class Matrix can be multiplied via the * operator, 
i.e. C = A * B should work To do this, implement __mul__(self, other) and return a new Matrix instance.
https://en.wikipedia.org/wiki/Matrix_(mathematics)#Matrix_multiplication
'''
#a = [['abc', 1], ['c', 1]]
#len([[]][0])

class Matrix:

    def __init__(self, matrix):
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise AssertionError
#        for i in range(2):
#            for j in range(2):
#                if type(matrix[i][j]) != int or type(matrix[i][j]) != float:
#                    raise ValueError
        self.__matrix = matrix
        # Implement this function and perform required checks
        # create adequate instance variables and check whether they should be private or public
        self.__rows=[matrix[i][:] for i in range(2)]
        self.__columns=[[matrix[i][j] for i in range(2)] for j in range(2)]

    # To implement the required functionality, you will also have to implement two more
    # of the special functions that include a double underscore as per the task description.
    def __add__(self, other):
        # two instances A and B of class Matrix can be added via the + operator,
        #i.e. C = A + B should work To do this, implement __add__(self, other) and return a new Matrix instance.
        tmp = []
        for j in range(len(self.__matrix)):
            tmp.append([])
            for k in range(len(self.__matrix[0])):
                tmp[j].append(self.__matrix[j][k] + other.__matrix[j][k])
        return Matrix(tmp)

    def __multList(self, l1, l2):
        if len(l1)==len(l2):
            return sum([l1[i]*l2[i] for i in range(len(l1))])

    def __mul__(self, other):
    #- make sure that two instancesA and B of class Matrix can be multiplied via the * operator, 
    #i.e. C = A * B should work To do this, implement __mul__(self, other) and return a new Matrix instance.
        tmp = []
        for i in range(len(self.__rows)):
            rows = []
            for j in range(len(other.__columns)):
                rows.append(self.__multList(other.__columns[j], self.__rows[i]))
            tmp.append(rows)
        return Matrix(tmp)

    def __repr__(self) -> str:    # DO NOT CHANGE the functions below! Consider also implementing __repr__ and __str__ for nice printing
        return repr(self.__matrix)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.__matrix]))




# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    M = Matrix([[5,5],[5,5]])
    T = Matrix([[5,5],[5,5]])
    print(M)
    print(M == T)
    d = {M: "1", T: "2"}
    d.update({M: "3"})
    print(d)
    print(M+T)
    print(M*T)