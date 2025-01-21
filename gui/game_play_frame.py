
import customtkinter as ctk
from gui.config import Config
from gui.sudoku_grid_frame import SudokuGrid

class GamePlayFrame(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(
            master,
            width= Config.primary_frame_width,
            height= Config.primary_frame_height,
            fg_color= Config.primary_frame_color
        )
        #Timer
        Timer(self).pack(padx=(20,0))
        #Center Frame
        central_frame = ctk.CTkFrame(self,fg_color= Config.primary_frame_color)
        central_frame.pack(pady=(30,0))
        #Smaller Frame
        SmallFrame(central_frame).pack(side="left",padx=(0,10))
        #The sodoku grid
        SudokuGrid(central_frame,**kwargs).pack(side="left")
        #Number Frame
        NumberFrame(self).pack(pady=(40,0))
        
        self.pack_propagate(False)
class SmallFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(
            master,
            width=20,
            height=200,
            fg_color="red"
        )
        self.pack_propagate(False)
class NumberFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(
            master,
            height=30,
            width=400,
            fg_color="transparent"
        )
        self.grid_columnconfigure((0,1,2,3,4),weight=1)
        
        for i in range(9):
            row = i // 5  # First 5 numbers in row 0, next in row 1
            col = i % 5  # 5 columns per row
            button = NumberButton(self, text=str(i + 1))
            button.grid(row=row, column=col,padx=(10,0),pady=(0,10))
        self.pack_propagate(False)
        NumberButton(self, text="<-").grid(row=1, column=4,padx=(10,0),pady=(0,10))


class NumberButton(ctk.CTkButton):
    def __init__(self,master,text):
        super().__init__(
            master,
            text=text,
            border_width=1,
            border_color="grey",
            fg_color="transparent",
            text_color="#455263",
            height=40,
            width=40
        )
        self.bind("<Button-1>",self.on_click)

    def on_click(self,event):
        pass

class Timer(ctk.CTkLabel):
    def __init__(self,master):
        super().__init__(
            master,
            text="45 S",
            font=('Arial', 18)
        )
