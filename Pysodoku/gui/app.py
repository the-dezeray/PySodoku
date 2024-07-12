from typing import Tuple
import pywinstyles
from Pysodoku.gui.left_frame import LeftFrame
from Pysodoku.gui.welcome_menu import WelcomeMenu
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


if __name__ == "__main__":
    app = APP()
    app._state_before_windows_set_titlebar_color = 'zoomed'
    app.mainloop()
