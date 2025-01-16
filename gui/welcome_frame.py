import customtkinter as ctk
from gui.blank_sudoku_frame import BlankSudokuGrid
from gui.game_play_frame import GamePlayFrame
from gui.config import Config
import os
from PIL import Image ,ImageTk
from gui.icons import skull

class WelcomeFrame(ctk.CTkFrame):
      def __init__(self,master):
            super().__init__(
                  master,
                  height=Config.primary_frame_height,
                  width=Config.primary_frame_width,
                  fg_color= Config.primary_frame_color
                  )
            self.master =master
            self.pack_propagate(False)
            self.current = Config.previous_game_level
            #The basic sodoku frame
            self.sudoku_grid : ctk.CTkFrame= BlankSudokuGrid(self)
            self.sudoku_grid.pack(pady = (50,0))

            self.levels =["easy","medium","hard","extreme","madness"]
            
            self.new_game = ctk.CTkButton(self,text="",image=skull,fg_color ="transparent",text_color="#868bab")         
            self.new_game.pack(pady=(20,5))
            #Frame 
            self.level_select_frame =ctk.CTkFrame(self)
            self.level_select_frame.pack(anchor ="n",pady=(0,0))
            
            #Goto to the previous selected level button
            self.arrow(text = "<",command=lambda:self.switch_level(1))
        
            self.current_level ="easy"
            #Current Level Label 
            self.current_level_button = ctk.CTkButton(self.level_select_frame,text="easy",fg_color ="transparent",text_color="#455263")
            self.current_level_button.pack(padx=5 ,side="left")

            #Goto to the next level Button
            self.arrow(text = ">",command=lambda:self.switch_level(1))
            
            #Continue saved game
            #$if Config.saved_game_exists():
            self.continue_game_button = ctk.CTkButton(self,text="continue",command= lambda : self.master.render_frame(GamePlayFrame,level = self.current_level,is_existing = True),fg_color ="transparent",text_color="#455263")
            self.continue_game_button.pack(pady=(20,0))
            #Play a new game
            self.new_game = ctk.CTkButton(self,text="new game",command = lambda : self.master.render_frame(GamePlayFrame,level = self.current_level,is_existing = False),fg_color ="transparent",text_color="#868bab")         
            self.new_game.pack(pady=(20,0))

      def switch_level(self,distance):
            curr = self.levels.index(self.current_level) 
            if self.current_level =="medium":
                  d = 0
            curr += distance
            if curr < 0 :
                  curr =3 
            elif curr > 4 :curr =0 
            self.current_level =  self.levels[curr]
            
            self.current_level_button.configure(text =  self.current_level)
            if Config.saved_game_exists():
                  pass
      def button(self,text,cmomand):
             ctk.CTkButton(self,
                           text="new game",command = lambda : self.master.render_frame(GamePlayFrame,level = self.current_level,is_existing = False),fg_color ="transparent",text_color="#868bab")         

      def arrow(self,text,command):
            ctk.CTkButton(self.level_select_frame,
                        text=text,
                        width=10,
                        height=10,
                        command=command,
                        fg_color ="transparent",
                        text_color="#455263"
            ).pack(padx=(10,5),side="left")