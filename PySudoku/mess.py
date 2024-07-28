import customtkinter 

app = customtkinter.CTk()
def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off",)
switch.pack()
app.mainloop()