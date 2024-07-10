from typing import Tuple
import customtkinter as ctk
class APP(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku")
        self.geometry("540x540")
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
