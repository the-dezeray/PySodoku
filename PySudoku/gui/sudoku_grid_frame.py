import threading
import keyboard
import customtkinter as ctk
from core.sodoku import generate,solved_sodoku


class SudokuGrid(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent)

        self.arry = None
        self.solved_array = None
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.thread = []
        self.stop_event  = threading.Event()
        
        self.highlight_selected_color : str= "blue"
        self.highlight_similar: str = "yellow"
        self.highlight_error_color: str = "red"
        self.highlight_duplicate : str= "red"
        self.hihglight_in_row_col_box : str= "yellow"
        self.create_grid()
    

    def fill(self,object:ctk.CTkButton):
        arry = ["1","2","3","4","5","6","7","8","9","backspace"]
        while True:
            a =keyboard.read_key()
            if str(a) in arry:
                if len(self.thread) > 1 and object.cget("text") in arry:
                    self.thread.pop(0)
                    return 0
                else:
                    self.update_sudoku_button(object,a)             
        return None
    
    def update_sudoku_button(self,button:ctk.CTkButton,input_value:str):

        button.configure(text=input_value)
        cur_row = button.row
        cur_col = button.col
        #if  value is incorrect apply effects on the recent entriie
        if int(input_value) != self.solved_array[cur_row][cur_col]:
            button.configure(fg_color =self.highlight_error_color)
            #object.configure(text_color="red")

            #highlight duplicates in row
            for i in range(9):
                _duplicate_entry :ctk.CTkButton= self.entries[cur_row][i]  

                if int(input_value) == _duplicate_entry.cget("text"):  
                    _duplicate_entry.configure(fg_color = self.highlight_duplicate,text_color = "")
            
            #highlight duplicates in row
            for i in range(9):
                _duplicate_entry = self.entries[i][cur_col]

                if int(input_value) ==  _duplicate_entry.cget("text"):
                    _duplicate_entry.configure(fg_color = self.highlight_duplicate)
                    

            #highlight similar in 3 x 3 box
            box_start_row = (cur_row // 3) * 3
            box_start_col = (cur_col // 3) * 3
            for row in range(box_start_row, box_start_row + 3):
                for col in range(box_start_col, box_start_col + 3):
                    _duplicate_entry =  self.entries[i][cur_col]

                    if int(input_value) ==  _duplicate_entry.cget("text"):
                        _duplicate_entry.configure(fg_color = self.highlight_duplicate)


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

