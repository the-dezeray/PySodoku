import customtkinter as ctk
from gui.config import Config
def nav_btn (master,text,command,image):
        return ctk.CTkButton(master=master,fg_color="transparent",compound = "left", anchor = "w",text=text, command=command, image=image,font=ctk.CTkFont(weight="normal"),text_color=Config.nav_btn_text_color)  