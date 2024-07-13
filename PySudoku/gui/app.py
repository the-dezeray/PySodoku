from typing import Tuple
import pywinstyles
from gui.left_frame import LeftFrame
from gui.welcome_menu import WelcomeMenu
from gui.game_play_frame import GamePlayFrame
import customtkinter as ctk

class APP(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Left menu
        self.left_menu = LeftFrame(self)
        self.left_menu.pack(side="left")      
    
        #The is the a secondary frame when new winwos are made they replace this .. from the settings window , to the leader board or any other replace this frame    
        self.right_menu = WelcomeMenu(self)
        self.right_menu.pack(side="right",padx=(0,100))

    def render_new_game(self,level=None):
        self.right_menu.destroy()
        self.right_menu =  GamePlayFrame(self.master)
        self.right_menu.pack()
    
    def render_exisiting_game(self,level=None):
        self.right_menu.destroy()
        self.right_menu =  GamePlayFrame(self.master)

def render_game():
    app = APP()
    app._state_before_windows_set_titlebar_color = 'zoomed'
    app.mainloop()

if __name__ == "__main__":
    app = APP()
    app._state_before_windows_set_titlebar_color = 'zoomed'
    app.mainloop()
