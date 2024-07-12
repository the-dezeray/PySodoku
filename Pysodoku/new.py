from typing import Tuple
import pywinstyles
from left_frame import LeftFrame
import customtkinter as ctk
from basic_sodoku_grid import SudokuGrid
class APP(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku")
        self.geometry("1280x720")
        

        self.c = ctk.CTkFrame(self,height=600,width=1000)
        self.c.pack_propagate(False)
        

        self.left_menu = LeftFrame(self)
        



        self.left_menu.pack(side="left")

      
        self.c.pack(side="right",padx=(0,100))


        self.frame= SudokuGrid(self.c)
        self.frame.pack()

        self.number_frame=ctk.CTkFrame(self.c)

        self.number_frame.pack(anchor ="n",pady=(40,0))

        self.aa = ctk.CTkButton(self.number_frame,text="<",width=10,height=10)
        self.aa.pack(padx=(5,10),side="left")
        self.bb = ctk.CTkButton(self.number_frame,text="easy")
        self.bb.pack(padx=5 ,side="left")
        self.cc = ctk.CTkButton(self.number_frame,text=">",width=10)
        self.cc.pack(padx=(10,5),side="left")
        self.other1 = ctk.CTkButton(self.c,text="continue")
        self.other1.pack(pady=(20,0))
        self.other = ctk.CTkButton(self.c,text="new game")
        self.other.pack(pady=(20,0))


if __name__ == "__main__":
    app = APP()
    app.mainloop()
