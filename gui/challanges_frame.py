import customtkinter as ctk
from gui.config import Config

class ChallangesFrame(ctk.CTkFrame):
    def __init__(self,master):

        super().__init__(
            master,
            width= Config.primary_frame_height,
            height = Config.primary_frame_width)