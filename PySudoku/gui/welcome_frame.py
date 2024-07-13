import customtkinter as ctk
from gui.blank_sudoku_frame import BlankSudokuGrid
from gui.game_play_frame import GamePlayFrame
class WelcomeFrame(ctk.CTkFrame):
        def __init__(self,master):
            super().__init__(master,height=600,width=1000)
            self.master =master
            self.pack_propagate(False)

            #The basic sodoku frame
            self.sudoku_grid : ctk.CTkFrame= BlankSudokuGrid(self)
            self.sudoku_grid.pack()
            
            #Frame 
            self.level_select_frame =ctk.CTkFrame(self)
            self.level_select_frame.pack(anchor ="n",pady=(40,0))

            #Goto to the previous selected level button
            self.previous_level_button = ctk.CTkButton(self.level_select_frame,text="<",width=10,height=10)
            self.previous_level_button.pack(padx=(5,10),side="left")
            
            #Current Level Label 
            self.current_level_button = ctk.CTkButton(self.level_select_frame,text="easy")
            self.current_level_button.pack(padx=5 ,side="left")

            #Goto to the next level Button
            self.next_level_button = ctk.CTkButton(self.level_select_frame,text=">",width=10)
            self.next_level_button.pack(padx=(10,5),side="left")

            #Continue saved game
            self.continue_game_button = ctk.CTkButton(self,text="continue")
            self.continue_game_button.pack(pady=(20,0))
            #Play a new game
            self.new_game = ctk.CTkButton(self,text="new game",command=lambda : self.master.render_new_game(level = None))         
            self.new_game.pack(pady=(20,0))



