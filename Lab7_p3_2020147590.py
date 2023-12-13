
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum


class list_D2(list):
    def __init__(self, arr):
        if not isinstance(arr, list) or not all(isinstance(row, list) for row in arr):
            raise not2DError()

        rows, cols = len(arr), len(arr[0])
        if any(len(row) != cols for row in arr):
            raise unevenListError()

        super().__init__(arr)

    def __str__(self):
        return f'list_2D: {len(self)}*{len(self[0])}'

    def transpose(self):
        return list_D2([[self[j][i] for j in range(len(self))] for i in range(len(self[0]))])

    def __matmul__(self, other):
        if len(self[0]) != len(other):
            raise improperMatrixError()

        result = [[mul1d(row, col) for col in zip(*other)] for row in self]
        return list_D2(result)

    def avg(self):
        flatten_matrix = [item for row in self for item in row]
        return sum(flatten_matrix) / len(flatten_matrix)