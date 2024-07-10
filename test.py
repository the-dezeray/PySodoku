import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("600x400")  # Set a fixed size for the window

# Create the left, center, and right frames with different sizes
left_frame = tk.Frame(root, width=100, height=100, bg='red')
center_frame = tk.Frame(root, width=150, height=150, bg='green')
right_frame = tk.Frame(root, width=100, height=100, bg='blue')

# Create spacer frames for proper alignment
left_spacer = tk.Frame(root, width=50)
right_spacer = tk.Frame(root, width=50)

# Pack the frames
left_frame.pack(side='left', padx=5, pady=5)
left_spacer.pack(side='left', expand=True)  # Expands to fill space between left and center
center_frame.pack(side='left', padx=5, pady=5)
right_spacer.pack(side='left', expand=True)  # Expands to fill space between center and right
right_frame.pack(side='left', padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
