from PIL import Image, ImageTk
import os
import customtkinter as ctk
from gui.templates import nav_button
from gui.settings_frame import SettingsFrame
from gui.challanges_frame import ChallangesFrame
from gui.game_play_frame import GamePlayFrame
from gui.leaderboard_frame import LeaderBoardFrame
from gui.welcome_frame import WelcomeFrame
class LeftFrame(ctk.CTkFrame):
    def __init__(self,master):

        file_path = os.path.dirname(os.path.realpath(__file__))
        settings  =ctk.CTkImage(Image.open(file_path +"/assets/settings.png"),size = (20,20))
        leaderboard  =ctk.CTkImage(Image.open(file_path +"/assets/leaderboard.png"),size = (20,20))
        close  =ctk.CTkImage(Image.open(file_path +"/assets/close.png"),size = (20,20))
        about  =ctk.CTkImage(Image.open(file_path +"/assets/about-us.png"),size = (20,20))
        challange  =ctk.CTkImage(Image.open(file_path +"/assets/challange.png"),size = (20,20))
        play  =ctk.CTkImage(Image.open(file_path +"/assets/play.png"),size = (20,20))

        super().__init__(master=master,height =600,width=200,fg_color="#030404")
        self.pack_propagate(False)
        self.heading = ctk.CTkButton(self,text="S  O D O K U",text_color="#e9edf0",fg_color="transparent")
        self.heading.pack(pady =(10,0),anchor = "w",padx = 10)

        self.bar = ctk.CTkProgressBar(self,progress_color="#e9edf0",width= 100,height = 3)
        self.bar.pack(pady =(5,40),padx = 40,anchor = "w")
                      
        self.main = nav_button(self,"Gamplay",play,WelcomeFrame)
        self.main.pack(pady =10,padx =10)
        
        self.challanges = nav_button(self,"Challanges",challange,ChallangesFrame)
        self.challanges.pack(pady=10,padx =2)

        self.leaderboard = nav_button(self,"Leaaderboard",leaderboard,LeaderBoardFrame)
        self.leaderboard.pack(pady=10,padx =2)
        



        self.settings = nav_button(self,"Settings",settings,SettingsFrame)
        self.settings.pack(pady=10,padx =2)

        self.about_us=nav_button(self,"About us",about)
        self.about_us.pack(pady=5,padx =2,side = "bottom")
        self.exit= nav_button(self,"Exit",close)
        self.exit.pack(pady=(0,5),padx =2,side = "bottom")

    
class NavigationButton(ctk.CTkButton):
    def __init__(self, master,text,command):
        pass
    
