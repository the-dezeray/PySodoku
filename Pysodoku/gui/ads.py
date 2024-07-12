from typing import Tuple
import customtkinter as ctk
import threading
import keyboard
from core.sodoku import generate,solved_sodoku
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
        self.solved_array = None
        super().__init__(master=parent)
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.thread = []
        self.stop_event  = threading.Event()

        self.arry = None
    def fill(self,object:ctk.CTkButton):
        arry = ["1","2","3","4","5","6","7","8","9","backspace"]
        while True:
            a =keyboard.read_key()
            if str(a) in arry:
                if len(self.thread) > 1 and object.cget("text") in arry:
                    self.thread.pop(0)
                    return 0
                else:
                    object.configure(text=a)
                    b= self.solved_array
                    if int(a) != b[object.row][object.col]:
                        object.configure(fg_color ="red")
                        for i in range(9):
                            t =self.entries[object.row][i].cget("text")
                            if int(a) ==  t:
                                self.entries[object.row][i].configure(fg_color = "red")
                        for i in range(9):
                            if int(a) ==  self.entries[i][object.col].cget("text"):
                                self.entries[i][object.col].configure(fg_color = "red")
                        box_start_row = (object.row // 3) * 3
                        box_start_col = (object.col // 3) * 3
                        for row in range(box_start_row, box_start_row + 3):
                            for col in range(box_start_col, box_start_col + 3):
                                if int(a) ==  self.entries[i][object.col].cget("text"):
                                    self.entries[i][object.col].configure(fg_color = "red")             

        return None
        
    def another(self,event):
        object= event.widget.master
        arry = ["1","2","3","4","5","6","7","8","9","backspace"]
        while True:
            a =keyboard.read_key()
            if str(a) in arry:
                if len(self.thread) > 1 and object.cget("text") in arry:
                    self.thread.pop(0)
                    return 0
                else:
                    object.configure(text=a)
                    if int(a) != self.solved_array[object.row][object.col]:
                        object.configure(text_color = "red")
        return None
    def highlight_related(self, event):

        widget = event.widget
        selected_row = widget.master.row
        selected_col = widget.master.col
        
        # Highlight the row
        for col in range(9):
            self.entries[selected_row][col].configure(fg_color='yellow')
        
        # Highlight the column
        for row in range(9):
            self.entries[row][selected_col].configure(fg_color='yellow')
        
        # Highlight the 3x3 box
        box_start_row = (selected_row // 3) * 3
        box_start_col = (selected_col // 3) * 3
        for row in range(box_start_row, box_start_row + 3):
            for col in range(box_start_col, box_start_col + 3):
                self.entries[row][col].configure(fg_color='yellow')
        
        # Highlight the selected cell differently
        widget.configure(fg_color='orange')

    def reset_highlight(self, event):
        # Reset all cells' background color
        for row in range(9):
            for col in range(9):
                self.entries[row][col].configure(fg_color='white')
    def insert_input(self,row,col):

        t = threading.Thread(target=self.fill,args=[self.entries[row][col]],daemon=True)
        t.start()
        self.thread.append(t)
    def insert_input2(self,event):

        t = threading.Thread(target=self.fill,args=[event.widget.master],daemon=True)
        t.start()
        self.thread.append(t)
    def create_grid(self):

        arr =generate()
        self.solved_array = solved_sodoku(arr)
        for row in range(9):
            for col in range(9):
                text = arr.pop(0)
                if text == 0: text = ""
                entry = ctk.CTkButton(self, width=40,height= 40, text=text,font=('Arial', 18), border_width=1,corner_radius=4)
                entry.row = row
                entry.col = col
                entry.grid(row=row, column=col, padx=(2, 2) if col % 3 != 2 else (2, 6), pady=(2, 2) if row % 3 != 2 else (2, 6))
                entry.bind("<Button-1>", self.highlight_related)
                entry.bind("<Button-1>",self.insert_input2)
                self.entries[row][col] = entry

        # Create thicker lines for separating 3x3 grids
        for i in range(1, 9):
            if i % 3 == 0:
                self.grid_rowconfigure(i, minsize=10)
                self.grid_columnconfigure(i, minsize=10)

if __name__ == "__main__":
    app = APP()
    app.mainloop()

