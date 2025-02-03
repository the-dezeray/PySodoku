from PIL import Image, ImageTk
import os
import customtkinter as ctk

    
def get_path():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

file_path = os.path.join(get_path(), "assets")

settings = ctk.CTkImage(Image.open(os.path.join(file_path, "settings.png")), size=(20, 20))
leaderboard = ctk.CTkImage(Image.open(os.path.join(file_path, "leaderboard.png")), size=(20, 20))
close = ctk.CTkImage(Image.open(os.path.join(file_path, "close.png")), size=(20, 20))
about = ctk.CTkImage(Image.open(os.path.join(file_path, "about-us.png")), size=(20, 20))
challange = ctk.CTkImage(Image.open(os.path.join(file_path, "challange.png")), size=(20, 20))
play = ctk.CTkImage(Image.open(os.path.join(file_path, "play.png")), size=(20, 20))
skull = ctk.CTkImage(Image.open(os.path.join(file_path, "skull.png")), size=(20, 20))                                            
