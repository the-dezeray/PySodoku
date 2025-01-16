"""i towkrs"""
import customtkinter as ctk
from gui.config import Config


class SettingsFrame(ctk.CTkFrame):
    def __init__(self,master):

        super().__init__(
            master,
            width=800,
            height = Config.primary_frame_width,
            fg_color= Config.primary_frame_color
            )
        
        self.pack_propagate(False)       
        self.heading = ctk.CTkButton(self,text="Settings",text_color=Config.default_chapter_label_text_color,font = ctk.CTkFont(size = 15),fg_color="transparent")
        self.heading.pack(pady =(40,40),anchor = "w",padx = 10)

        switch(master=self,text = "Highlight errora")
        switch(master=self,text = "Animations and effects")
        switch(master=self,text = "Timer")
        switch(master=self,text = "Online status Enabled")
        switch(master=self,text = "Enable note taking")
        switch(master=self,text = "Auto clear notes")
        switch(master=self,text = "Undo moves")
        button_a(master=self,text = "Choose language")
        option_fr(master=self,text = "appearance mode")
       
        
def switch(master,text):
    frame = ctk.CTkFrame(master,fg_color= "transparent",width= 400,height = 30)
    frame.pack_propagate(False)
    buttons(master = frame,text=text).pack(side = "left")
    ctk.CTkSwitch(frame,text=None,fg_color = "#434e5e",button_color="#6978c0").pack(side = "right",padx = (10,0))
    frame.pack(anchor  ="w",padx = (100,0),pady=(0,10))

def button_a(master,text):
    frame = ctk.CTkFrame(master,fg_color= "transparent",width= 400,height = 30)
    frame.pack_propagate(False)
    buttons(master = frame,text=text).pack(side = "left")
    ctk.CTkButton(frame,text="english").pack(side = "right",padx = (10,0))
    return frame
    
def option_fr(master,text):
    frame = ctk.CTkFrame(master,fg_color= "transparent",width= 400,height = 30)
    frame.pack_propagate(False)
    buttons(master = frame,text=text).pack(side = "left")
    ctk.CTkOptionMenu(frame, values=["option 1", "option 2"]).pack(side = "right",padx = (10,0))
    return frame

def buttons(master,text):
    return ctk.CTkLabel(
        master=master,
        text= text,
        text_color= Config.default_chapter_label_text_color
    ) 