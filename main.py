from typing import Tuple
import customtkinter as ctk
class APP(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku")
        self.geometry("540x540")
        self.c = ctk.CTkFrame(self,fg_color="transparent")
        self.c.pack(fill ="x",anchor="n",pady=(40,0))
        self.left_menu = ctk.CTkFrame(self.c,height=300,width=200)
        self.left_menu.pack_propagate(False)
        
        self.center_frame= ctk.CTkFrame(self.c)
 

        self.right = ctk.CTkFrame(self.c,height=300,width=200)
        self.right.pack_propagate(False)
        
        self.left_spacer = ctk.CTkFrame(self.c, width=50)
        self.right_spacer = ctk.CTkFrame(self.c, width=50)
        self.left_menu.pack(side="left")
        self.left_spacer.pack(side='left', expand=True) 
        self.center_frame.pack(side="left")
        self.right_spacer.pack(side='left', expand=True) 
        self.right.pack(side="left")

        self.smaller_frame=ctk.CTkFrame(self.center_frame,width=20,height=200)
        self.smaller_frame.pack_propagate(False)
        self.smaller_frame.pack(side="left",padx=(0,10))
        self.frame= SudokuGrid(self.center_frame)
        self.frame.pack(side="left")
        self.number_frame=ctk.CTkFrame(self,height=30,width=400)
        self.number_frame.pack_propagate(False)
        self.number_frame.pack(anchor ="n",pady=(40,0))
        self.other = ctk.CTkButton(self,text="play game")
        self.other.pack(pady=(10,0))
class SudokuGrid(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent)
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = ctk.CTkButton(self, width=40,height= 40, text="  ",font=('Arial', 18), border_width=1,corner_radius=4)
                entry.grid(row=row, column=col, padx=(2, 2) if col % 3 != 2 else (2, 6), pady=(2, 2) if row % 3 != 2 else (2, 6))
                self.entries[row][col] = entry

        # Create thicker lines for separating 3x3 grids
        for i in range(1, 9):
            if i % 3 == 0:
                self.grid_rowconfigure(i, minsize=10)
                self.grid_columnconfigure(i, minsize=10)

if __name__ == "__main__":
    app = APP()
    app.mainloop()
