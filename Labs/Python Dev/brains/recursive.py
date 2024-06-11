import numpy as np
# n(n-1)(n-2)(n-3)....(2)(1)

# 5(5-1)(5-2)(5-3)(5-4)
# 5(4)(3)(2)(1)

# n(n-1)!
# 5(4)! -> (5)(4)(3)! -> (5)(4)(3)(2)! -> (5)(4)(3)(2)(1)!

def factorial(n):
    print(f"calculating factorial of {n}")
    # terminating condition
    if n==1 or n==0:
        return 1
    # function body
    # recursive call
    result = n * factorial(n-1)
    print(f"factorial({n})={result}")
    return result
    
def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    else:
        sign = 1
        result = 0
        for selected_col in range(size):
            sub_matrix = []
            for current_row in range(1,size):
                sub_row=[]
                for current_col in range(size):
                    if current_col != selected_col:
                        sub_row.append(matrix[current_row][current_col])
                sub_matrix.append(sub_row)
            result += sign * matrix[0][selected_col] * determinant(sub_matrix)
            sign *= -1
        return result


if __name__ == '__main__':
    # result = factorial(5)
    # print(f"Factorial of 5 is {result}")

    myMatrix = [[1,2,3,4],
                [1,2,5,1],
                [1,5,6,3],
                [1,1,2,1],]
    myMatrixDeterminent = determinant(myMatrix)
    print(myMatrixDeterminent)
    print(round(np.linalg.det(myMatrix)))