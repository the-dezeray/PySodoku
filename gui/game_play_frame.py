
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

        ctk.CTkLabel(self,text="45 S",font=('Arial', 18)).pack(padx=(20,0))
        
        self.center_frame= ctk.CTkFrame(self,fg_color= Config.primary_frame_color)
        self.center_frame.pack(pady=(30,0))

        self.smaller_frame=ctk.CTkFrame(self.center_frame,width=20,height=200,fg_color= Config.primary_frame_color)
        self.smaller_frame.pack_propagate(False)
        self.smaller_frame.pack(side="left",padx=(0,10))
        
        self.frame= SudokuGrid(self.center_frame,**kwargs)
        self.frame.pack(side="left")

        self.number_frame=ctk.CTkFrame(self,height=30,width=400)
        self.number_frame.pack_propagate(False)
        self.number_frame.pack(pady=(40,0))

        self.pack_propagate(False)
