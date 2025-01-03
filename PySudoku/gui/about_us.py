import customtkinter as ctk
from gui.blank_sudoku_frame import BlankSudokuGrid
from gui.game_play_frame import GamePlayFrame
from gui.config import Config
import os
from PIL import Image ,ImageTk

class AboutUs(ctk.CTkFrame):
      def __init__(self,master):
            super().__init__(
                  master,
                  height=Config.primary_frame_height,
                  
                  width=Config.primary_frame_width,
                  fg_color= Config.primary_frame_color
                  )