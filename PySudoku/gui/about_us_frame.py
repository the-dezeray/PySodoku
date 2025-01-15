"""i towkrs"""
import customtkinter as ctk
from gui.config import Config

class AboutUsFrame(ctk.CTkFrame):
    def __init__(self,master):

        super().__init__(
            master,
            width=800,
            height = Config.primary_frame_width,
            fg_color= Config.primary_frame_color
            )
        