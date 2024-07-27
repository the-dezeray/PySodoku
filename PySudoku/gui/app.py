from typing import Tuple

from gui.left_frame import LeftFrame
from gui.welcome_frame import WelcomeFrame
from gui.game_play_frame import GamePlayFrame
import customtkinter as ctk
from gui.settings_frame import SettingsFrame
from gui.leaderboard_frame import LeaderBoardFrame
from gui.challanges_frame import ChallangesFrame
from gui.game_ending_frame import GameEndingFrame
from gui.config import Config
ctk.set_appearance_mode("Dark") 
class APP(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Left menu
        self.left_menu : ctk.CTkFrame= LeftFrame(self)
        self.left_menu.pack(side="left",fill ="y",expand =True,)      
    
        #The is the a secondary frame when new winwos are made they replace this .. from the settings window , to the leader board or any other replace this frame    
        self.right_menu = WelcomeFrame(self)
        self.right_menu.pack(side="left",expand= True,fill = "both")

    #Load a new sodoku game
    def render_sudoku_grid(self,level=None,is_existing = False):
        self.right_menu.destroy()
        self.right_menu =  GamePlayFrame(self.master, level ,  is_existing)
        self.right_menu.pack(side="right",padx=(0,100),pady = (100,0))
    
    def render_settings(self):
        self.right_menu.destroy()
        self.right_menu = SettingsFrame(master = self.master)
        self.right_menu.pack(side="right",padx=(0,100),pady = (100,0))
        
    def render_leaderboard(self):
        self.right_menu.destroy()
        self.right_menu = LeaderBoardFrame(master = self.master)
        self.right_menu.pack(side="right",padx=(0,100),pady = (100,0))

    def render_game_ending_frame(self,state:str = "win"):
        self.right_menu.destroy()
        self.right_menu = GameEndingFrame(master = self.master,state=state)
        self.right_menu.pack(side="right",padx=(0,100),pady = (100,0))
    

    def render_challanges(self):
        self.right_menu.destroy()
        self.right_menu = ChallangesFrame(master = self.master)
        self.right_menu.pack(side="right",padx=(0,100),pady = (100,0))




def start_application():

    app = APP()
    #app._state_before_windows_set_titlebar_color = 'zoomed'
    app.mainloop()

if __name__ == "__main__":
    start_application()