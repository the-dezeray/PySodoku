
import customtkinter as ctk
from gui.settings_frame import SettingsFrame
from gui.challanges_frame import ChallangesFrame
from gui.leaderboard_frame import LeaderBoardFrame
from gui.welcome_frame  import WelcomeFrame
from gui.about_us_frame import AboutUsFrame
from gui.icons import file_path,settings,leaderboard,close,about,challange,play
from gui.config import Config
from gui.btn import nav_btn


class LeftFrame(ctk.CTkFrame):
    def __init__(self,master):

        super().__init__(master=master,height =600,width=200,fg_color="#030404")
        self.pack_propagate(False)

        def nav_btn(text,command =None,icon = None):
            return ctk.CTkButton(self,text=text,text_color=Config.nav_btn_text_color,fg_color="transparent")
    
        self.heading = nav_btn(text="S  O D O K U")
        self.heading.pack(pady =(10,0),anchor = "w",padx = 10)
        self.bar = ctk.CTkProgressBar(self,progress_color=Config.nav_btn_progress_color,width= 100,height = 3)
        self.bar.pack(pady =(5,40),padx = 40,anchor = "w")

        render =  self.master.render_frame
        place_navigation_button(master=self, text="Gameplay", command=lambda: render(WelcomeFrame), image=play)
        place_navigation_button(master=self, text="Challanges", command=lambda: render(ChallangesFrame), image=challange)
        place_navigation_button(master=self, text="Leaderboard",command=lambda: render(LeaderBoardFrame), image=leaderboard)
        place_navigation_button(master=self, text="Settings", command=lambda: render(SettingsFrame), image=settings)
        place_navigation_button(master=self, text="About us", command=lambda: render(AboutUsFrame), image=about)
        place_navigation_button(master=self, text="Exit", command=lambda: exit(), image=close)



def place_navigation_button(master,text :str ,command,image: ctk.CTkImage):
    button = nav_btn(master=master,text=text,command = command,image = image)
    button.pack(pady =10,padx =2)
     
    