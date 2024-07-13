from typing import Tuple
import customtkinter as ctk
import threading
import keyboard
from core.sodoku import generate,solved_sodoku
from gui.sudoku_grid_frame import SudokuGrid
class GamePlayFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        ctk.CTkLabel(self,text="45 S",font=('Arial', 18)).pack(padx=(20,0))
        self.center_frame= ctk.CTkFrame(self)
        self.center_frame.pack(pady=(30,0))
        self.smaller_frame=ctk.CTkFrame(self.center_frame,width=20,height=200)
        self.smaller_frame.pack_propagate(False)
        self.smaller_frame.pack(side="left",padx=(0,10))
        self.frame= SudokuGrid(self.center_frame)
        self.frame.pack(side="left")
        self.number_frame=ctk.CTkFrame(self,height=30,width=400)
        self.number_frame.pack_propagate(False)
        
        self.number_frame.pack(pady=(40,0))
 

