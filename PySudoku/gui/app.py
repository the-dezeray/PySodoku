from typing import Tuple
import pywinstyles
from gui.left_frame import LeftFrame
from gui.welcome_frame import WelcomeFrame
from gui.game_play_frame import GamePlayFrame
import customtkinter as ctk

class APP(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Left menu
        self.left_menu = LeftFrame(self)
        self.left_menu.pack(side="left")      
    
        #The is the a secondary frame when new winwos are made they replace this .. from the settings window , to the leader board or any other replace this frame    
        self.right_menu = WelcomeFrame(self)
        self.right_menu.pack(side="right",padx=(0,100))

    #Load a new sodoku game
    def render_new_game(self,level=None):
        self.right_menu.destroy()
        self.right_menu =  GamePlayFrame(self.master)
        self.right_menu.pack()
    
    #Load an existing  sodoku game
    def render_exisiting_game(self,level=None):
        self.right_menu.destroy()
        self.right_menu =  GamePlayFrame(self.master)

    #Load the Settines frame on the secondary frame
    def render_settings():
        pass

    #Load the Leaderboard frame on the secondary frame
    def render_leaderboard():
        pass

    #Load the challanges frame on the secondary frame
    def render_challanges():
        pass
def render_game():
    app = APP()
    app._state_before_windows_set_titlebar_color = 'zoomed'
    app.mainloop()

if __name__ == "__main__":
    render_game()