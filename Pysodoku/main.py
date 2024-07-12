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
        

        self.c = ctk.CTkFrame(self,fg_color="transparent")
        self.c.pack(fill ="x",anchor="n",pady=(40,0))

        self.left_menu = LeftFrame(self.c)
        
        self.center_frame= ctk.CTkFrame(self.c)
        self.left_spacer = ctk.CTkFrame(self.c, width=50,fg_color="transparent")
        self.right_spacer = ctk.CTkFrame(self.c, width=50,fg_color="transparent")

        self.right = ctk.CTkFrame(self.c,height=300,width=200,fg_color="transparent")
        self.right.pack_propagate(False)
        

        self.left_menu.pack(side="left")
        self.left_spacer.pack(side='left', expand=True) 
        self.center_frame.pack(side="left")
        self.right_spacer.pack(side='left', expand=True) 
        self.right.pack(side="left")

        self.frame= SudokuGrid(self.center_frame)
        self.frame.pack(side="left")

        self.number_frame=ctk.CTkFrame(self)

        self.number_frame.pack(anchor ="n",pady=(40,0))

        self.aa = ctk.CTkButton(self.number_frame,text="<",width=10,height=10)
        self.aa.pack(padx=(5,10),side="left")
        self.bb = ctk.CTkButton(self.number_frame,text="easy")
        self.bb.pack(padx=5 ,side="left")
        self.cc = ctk.CTkButton(self.number_frame,text=">",width=10)
        self.cc.pack(padx=(10,5),side="left")
        self.other1 = ctk.CTkButton(self,text="continue")
        self.other1.pack(pady=(20,0))
        self.other = ctk.CTkButton(self,text="new game")
        self.other.pack(pady=(20,0))


if __name__ == "__main__":
    app = APP()
    app.mainloop()
