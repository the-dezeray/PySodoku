import numpy as np

from dokusan import solvers,generators
from dokusan.boards import Sudoku,BoxSize

def valid_colums(sudoku_list:list)->bool:

    if len(sudoku_list)!= 81: return False

    for column_index in range(9):
        column_list= [sudoku_list[row_index * 9 +column_index] for row_index in range(9)]
        if len(set(column_list)) != 9 or not all(1 <= num <= 9 for num in column_list):
            return False
    return True

def valid_rows(sudoku_list:list)->bool:
    if len(sudoku_list) != 81: return False
    for row_index in range(0,81,9):
        row_list = sudoku_list[row_index:row_index+9]
        if len(set(row_list)) != 9 or not all(1 <= num <= 9 for num in row_list):
            return False
    return True

def mutate_list(sudoku:list):
    mutation_map = {
        1: 2,
        2: 3,
        3:4,
        4:5,
        5:6,
        6:7,
        7:8,
        8:9,
        9:1,
    }
    mutated_list = [mutation_map.get(num) for num in sudoku] 
    return mutated_list

def solved_sodoku(arr):
    b =np.array(arr)
    b = b.reshape(9,9)

    b = sudoku = Sudoku.from_list(b,box_size =BoxSize(3,3))
    b = solvers.backtrack(b)
    b= list((str(b)))
    b = [int(a) for a in b]
    b = np.array(b)
    a =b.reshape(9,9)
    return a    

def generate():
    arr = list(str(generators.random_sudoku(avg_rank =150)))
    arr =[int(num) for num in arr]
    return arr