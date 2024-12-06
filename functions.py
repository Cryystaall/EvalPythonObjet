# functions.py

def several_zeros():
    return [0] * 10

def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros

def matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]

class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self._matrix == other._matrix
        return False

def my_sort(my_list: [int]) -> [int]:
    n = len(my_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


if __name__ == '__main__':
    print(several_zeros())
    print(several_zeros_custom(5))
    print(several_zeros_custom())
    
    result = matrix(2, 3)
    print(result[1][2])
    print(result[0])
    
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1 == m2)
    print(m1.get_value(1, 2))
    
    m3 = Matrix(3, 3)
    print(m1 == m3)

    my_list = [2, 6, 1, 9, 3]
    sorted_list = my_sort(my_list)
    print(sorted_list)
