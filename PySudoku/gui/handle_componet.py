import customtkinter as ctk
def get_master(parent):
    
    if  parent.master is not None :
        if isinstance(parent.master,ctk.CTk):
            return parent.master
        else:
            get_master(parent.master)
