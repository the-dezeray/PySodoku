import customtkinter as ctk
from gui.config import Config


class GameEndingFrame(ctk.CTkFrame):
    def __init__(self,master,state :str = "win"):

        super().__init__(
            master,
            width= Config.primary_frame_height,
            height = Config.primary_frame_width)