from dokusan import generators
import numpy as np


class Box:
    def __init__(self):
        self.value = 0
        self.possible_value = [1,2,3,4,5,6,7,8,9]
array = [Box()for _ in range(81)]



def valid_colums(sudoku_list:list)->bool:

    if len(sudoku_list)!= 81: return False

    for column_index in range(9):
        column_list= [sudoku_list[row_index * 9 +column_index] for row_index in range(9)]
        if len(set(column_list)) != 9 or not all(1 <= num <= 9 for num in column_list):
            return False
    return True
def valid_rows(sudoku_list:list):
    pass

arr = list(str(generators.random_sudoku(avg_rank =0)))
arr =[int(num) for num in arr]

print(valid_colums(arr))