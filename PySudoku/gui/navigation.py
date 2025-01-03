from PIL import Image, ImageTk
import os
import customtkinter as ctk

class LeftFrame(ctk.CTkFrame):
    def __init__(self,master):
        file_path = os.path.dirname(os.path.realpath(__file__))
        settings  =ctk.CTkImage(Image.open(file_path +"/settings.png"),size = (20,20))            
        file_path = os.path.dirname(os.path.realpath(__file__))
        leaderboard  =ctk.CTkImage(Image.open(file_path +"/leaderboard.png"),size = (20,20))            
        file_path = os.path.dirname(os.path.realpath(__file__))
        close  =ctk.CTkImage(Image.open(file_path +"/close.png"),size = (20,20))            
        file_path = os.path.dirname(os.path.realpath(__file__))
        about  =ctk.CTkImage(Image.open(file_path +"/about-us.png"),size = (20,20))            
        file_path = os.path.dirname(os.path.realpath(__file__))
        challange  =ctk.CTkImage(Image.open(file_path +"/challange.png"),size = (20,20))            
        file_path = os.path.dirname(os.path.realpath(__file__))
        play  =ctk.CTkImage(Image.open(file_path +"/play.png"),size = (20,20))            
                                                                    
        

        super().__init__(master=master,height =600,width=200,fg_color="#030404")
        self.pack_propagate(False)
        self.heading = ctk.CTkButton(self,text="S  O D O K U",text_color="#e9edf0",fg_color="transparent")
        self.heading.pack(pady =(10,0),anchor = "w",padx = 10)

        self.bar = ctk.CTkProgressBar(self,progress_color="#e9edf0",width= 100,height = 3)
        self.bar.pack(pady =(5,40),padx = 40,anchor = "w")
                      
        self.main = ctk.CTkButton(self,text="Gameplay",font=ctk.CTkFont(weight="bold"),image=play ,compound = "left",text_color="#434e5e",fg_color="transparent",anchor="w")
        self.main.pack(pady =10,padx =10)
        
        self.challanges = ctk.CTkButton(self,image=challange ,compound = "left",text ="Challanges",fg_color="transparent",anchor = "w",text_color="#434e5e")
        self.challanges.pack(pady=10,padx =2)

        self.leaderboard = ctk.CTkButton(self,text_color="#434e5e",image=leaderboard ,compound = "left",text ="Leaderboard",fg_color="transparent",anchor = "w")
        self.leaderboard.pack(pady=10,padx =2)
        from gui.settings_frame import SettingsFrame
        self.settings = ctk.CTkButton(self,text ="Settings",text_color="#434e5e",image=settings ,compound = "left",fg_color="transparent",anchor = "w",command= lambda:self.master.render_frame(frame = SettingsFrame))
        self.settings.pack(pady=10,padx =2)

        self.about_us= ctk.CTkButton(self,text ="About us",fg_color="transparent",image=about ,compound = "left",text_color="#434e5e",anchor = "w")
        self.about_us.pack(pady=5,padx =2,side = "bottom")
        self.exit= ctk.CTkButton(self,text ="Exit",fg_color="transparent",command=lambda: exit(),anchor = "w",text_color="#434e5e",image=close ,compound = "left")
        self.exit.pack(pady=(0,5),padx =2,side = "bottom")
class NavigationButton(ctk.CTkButton):
    def __init__(self, master,text,command):
        pass
    
