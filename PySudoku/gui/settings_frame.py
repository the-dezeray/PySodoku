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
        self.heading = ctk.CTkButton(self,text="Settings",text_color=Config.default_chapter_label_text_color,font = ctk.CTkFont(size = 15),fg_color="transparent",)
        self.heading.pack(pady =(40,0),anchor = "w",padx = 10)


  


        self.highlight_enabled = self.switch(master=self,text = "Highlight errora")
        self.highlight_enabled.pack(anchor  ="w",padx = (100,0),pady=(40,10))
        self.animations_enabled = self.switch(master=self,text = "Animations and effects")
        self.animations_enabled.pack(anchor  ="w",padx = (100,0),pady=(0,10))
        self.timer_enabled = self.switch(master=self,text = "Timer")
        self.timer_enabled.pack(anchor  ="w",padx = (100,0),pady=(0,10))
        self.online_status_enabled = self.switch(master=self,text = "Online status Enabled")
        self.online_status_enabled.pack(anchor  ="w",padx = (100,0),pady=(0,10))
        
        self.note_enabled = self.switch(master=self,text = "Enable note taking")
        self.note_enabled.pack(anchor  ="w",padx = (100,0),pady=(0,10))

        self.auto_clear_notes= self.switch(master=self,text = "Auto clear notes")
        self.auto_clear_notes.pack(anchor  ="w",padx = (100,0),pady=(0,10))

        self.undo = self.switch(master=self,text = "Undo moves")
        self.undo.pack(anchor  ="w",padx = (100,0),pady=(0,10))

        self.language = self.button_a(master=self,text = "Choose language")
        self.language.pack(anchor  ="w",padx = (100,0),pady=(0,10))

        self.apperance = self.option_fr(master=self,text = "appearance mode")
        self.apperance.pack(anchor  ="w",padx = (100,0),pady=(0,10))



        
    def switch(self,master,text):
        frame = ctk.CTkFrame(master,fg_color= "transparent",width= 400,height = 30)
        frame.pack_propagate(False)
        self.buttons(master = frame,text=text).pack(side = "left")
        ctk.CTkSwitch(frame,text=None,fg_color = "#434e5e",button_color="#6978c0").pack(side = "right",padx = (10,0))

        return frame

    def button_a(self,master,text):
        frame = ctk.CTkFrame(master,fg_color= "transparent",width= 400,height = 30)
        frame.pack_propagate(False)
        self.buttons(master = frame,text=text).pack(side = "left")
        ctk.CTkButton(frame,text="english").pack(side = "right",padx = (10,0))

        return frame
        
    def option_fr(self,master,text):
        frame = ctk.CTkFrame(master,fg_color= "transparent",width= 400,height = 30)
        frame.pack_propagate(False)
        self.buttons(master = frame,text=text).pack(side = "left")
        ctk.CTkOptionMenu(frame, values=["option 1", "option 2"]).pack(side = "right",padx = (10,0))


        return frame
    def buttons(self,master,text):
        return ctk.CTkLabel(
            master=master,
            text= text,
            text_color= Config.default_chapter_label_text_color
        ) 