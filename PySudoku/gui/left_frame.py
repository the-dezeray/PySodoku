import customtkinter as ctk

class LeftFrame(ctk.CTkFrame):
    def __init__(self,master):

        super().__init__(master=master,height =600,width=200)
        self.pack_propagate(False)

        self.main = ctk.CTkButton(self,text="main")
        self.main.pack(pady =10)
        
        self.challanges = ctk.CTkButton(self,text ="challanges")
        self.challanges.pack(pady=10)

        self.leaderboard = ctk.CTkButton(self,text ="leaderboard")
        self.leaderboard.pack(pady=10)

        self.settings = ctk.CTkButton(self,text ="settings")
        self.settings.pack(pady=10)
