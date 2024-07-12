
from Pysodoku.core.sodoku import generate
from dokusan import solvers
from dokusan.boards import Sudoku,BoxSize
import numpy as np
arr =generate()
print(arr)
b =np.array(arr)
b = b.reshape(9,9)

b = sudoku = Sudoku.from_list(b,box_size =BoxSize(3,3))
b = solvers.backtrack(b)
b= list((str(b)))
b = [int(a) for a in b]
b = np.array(b)
a =b.reshape(9,9)
print(a[3][4])
def des():
    pass