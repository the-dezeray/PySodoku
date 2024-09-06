import customtkinter as ctk
from gui.handle_componet import get_master

    
def nav_button(self,text,image : ctk.CTkImage,go_to =None):
    function = None
    if go_to is not None:
        master = get_master(self)
        function = lambda go_to = go_to: master.render_frame(go_to)
    return ctk.CTkButton(self,image= image ,compound = "left",text =text,fg_color="transparent",anchor = "w",text_color="#434e5e",command=function)