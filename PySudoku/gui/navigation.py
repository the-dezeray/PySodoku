<<<<<<< HEAD

import customtkinter as ctk
from gui.settings_frame import SettingsFrame
from gui.challanges_frame import ChallangesFrame
from gui.leaderboard_frame import LeaderBoardFrame
from gui.welcome_frame  import WelcomeFrame
from gui.icons import file_path,settings,leaderboard,close,about,challange,play
from gui.config import Config
from gui.btn import nav_btn
class LeftFrame(ctk.CTkFrame):
    def __init__(self,master):
=======
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
>>>>>>> 12cb7414d9e9a23e476ac5315b1c920f20f09f6b

        super().__init__(master=master,height =600,width=200,fg_color="#030404")
        self.pack_propagate(False)

<<<<<<< HEAD
        def nav_btn(text,command =None,icon = None):
            return ctk.CTkButton(self,text=text,text_color=Config.nav_btn_text_color,fg_color="transparent")
=======
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
>>>>>>> 12cb7414d9e9a23e476ac5315b1c920f20f09f6b
    
        self.heading = nav_btn(text="S  O D O K U")
        self.heading.pack(pady =(10,0),anchor = "w",padx = 10)
        self.bar = ctk.CTkProgressBar(self,progress_color=Config.nav_btn_progress_color,width= 100,height = 3)
        self.bar.pack(pady =(5,40),padx = 40,anchor = "w")

        render =  self.master.render_frame
        place_navigation_button(master=self, text="Gameplay", command=lambda: render(WelcomeFrame), image=play)
        place_navigation_button(master=self, text="Challanges", command=lambda: render(ChallangesFrame), image=challange)
        place_navigation_button(master=self, text="Leaderboard",command=lambda: render(LeaderBoardFrame), image=leaderboard)
        place_navigation_button(master=self, text="Settings", command=lambda: render(SettingsFrame), image=settings)
        place_navigation_button(master=self, text="About us", command=lambda: load_about_us(), image=about)
        place_navigation_button(master=self, text="Exit", command=lambda: exit(), image=close)



def place_navigation_button(master,text :str ,command,image: ctk.CTkImage):
    button = nav_btn(master=master,text=text,command = command,image = image)
    button.pack(pady =10,padx =2)
     
    