from typing import Tuple

from gui.navigation import LeftFrame
from gui.welcome_frame import WelcomeFrame
from gui.game_play_frame import GamePlayFrame
import customtkinter as ctk
from gui.settings_frame import SettingsFrame
from gui.leaderboard_frame import LeaderBoardFrame
from gui.challanges_frame import ChallangesFrame
from gui.game_ending_frame import GameEndingFrame
from gui.config import Config
ctk.set_appearance_mode(Config.color_mode) 

class APP(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.navigation : ctk.CTkFrame= LeftFrame(self)
        self.navigation.pack(side="left",fill ="y",expand =True,)      
    
        #The is the a secondary frame when new winwos are made they replace this .. from the settings window , to the leader board or any other replace this frame    
        self.frame : ctk.CTkFrame =WelcomeFrame(self)
        self.frame.pack(side="left",expand= True,fill = "both")

    
    def render_frame(self,frame : ctk.CTkFrame,**kwargs):
        self.frame.destroy()
        self.frame = frame(master = self,**kwargs)
        self.frame.pack(side="left",expand= True,fill = "both")

        
def start_application():
    app = APP()
    app.mainloop()

if __name__ == "__main__":
    start_application()