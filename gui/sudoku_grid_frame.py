import threading
import customtkinter as ctk
import time
from pynput.keyboard import Listener
from core.sodoku import generate, solved_sodoku
from gui.config import Config

class SudokuGrid(ctk.CTkFrame):

    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, fg_color="#050707")
        if "level" in kwargs:
            self.level = kwargs.pop("level")
        if "is_existing" in kwargs:
            self.is_existing = kwargs.pop("is_existing")
        self.arry = None
        self.solved_array = None
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.thread = []
        self.stop_event = threading.Event()
        self.time = ""
        self.error_count = 0
        self.key = None  # To store the key pressed
        self.create_grid()

        # Start the listener in a separate thread
        self.listener_thread = threading.Thread(target=self.start_listener)
        self.listener_thread.start()

    def start_listener(self):
        def on_press(key):
           
            self.key = str(key.char)  # Store the character of the key pressed
    # For special keys like backspace
            return True  # Keep listening

        with Listener(on_press=on_press) as listener:
            listener.join()  # Block the listener in the separate thread

    def fill(self, object: ctk.CTkButton):
        from pynput import keyboard
        arry = ["1", "2", "3", "4", "5", "6", "7", "8", "9", keyboard.Key.backspace ]
        
        while True:
            if self.key:  # Check if a key has been pressed
                print(f"key type {self.key}")
                
                if self.key in arry:
                    if len(self.thread) > 1 and object.cget("text") in arry:
                        self.thread.pop(0)
                        return 0
                    else:
                        self.update_sudoku_button(object, self.key)
                        
                        # Capture current game to YAML save file
                        Config.capture_game(
                            grid=self.grid_screenshot(),
                            level=self.level,
                            error_count=self.error_count,
                            time=self.time,
                            solved_grid=self.solved_array
                        )
                        
                    self.key = None  # Reset after handling the key press
            else:
                # If no key has been pressed, you can add a small delay to avoid busy-waiting
                time.sleep(0.1)
                
        return None
    
    def update_sudoku_button(self,button:ctk.CTkButton,input_value:str):
        if input_value == "backspace":
            input_value = ""
        button.configure(text=input_value)
        cur_row = button.row
        cur_col = button.col
        #if  value is incorrect apply effects on the recent entriie
        if int(input_value) != self.solved_array[cur_row][cur_col]:

            button.configure(text_color =Config.highlight_error_color)
            #object.configure(text_color="red") 
            #highlight duplicates in row
            for i in range(9):
                _duplicate_entry :ctk.CTkButton = self.entries[cur_row][i]  

                if int(input_value) == _duplicate_entry.cget("text"):  
                    _duplicate_entry.configure(text_color = Config.highlight_duplicate)
            #highlight duplicates in row
            for i in range(9):
                _duplicate_entry = self.entries[i][cur_col]

                if int(input_value) ==  _duplicate_entry.cget("text"):
                    _duplicate_entry.configure(text_color = Config.highlight_duplicate)
            #highlight similar in 3 x 3 box
            box_start_row = (cur_row // 3) * 3
            box_start_col = (cur_col // 3) * 3
            for row in range(box_start_row, box_start_row + 3):
                for col in range(box_start_col, box_start_col + 3):
                    _duplicate_entry =  self.entries[i][cur_col]

                    if int(input_value) ==  _duplicate_entry.cget("text"):
                        _duplicate_entry.configure(text_color=Config.highlight_duplicate)
        if self._grid_complete():
            self._game_won_event()

    def highlight_errors(self)->bool:
        for row in range(9):
            for col in range(9):
                value = self.entries[row][col].cget("text")
                if value == "" or value == " ":
                    continue
                solved = self.solved_array[row][col]
                a= int(value)
                b = int(solved)
                if int(value) !=  int(solved):
                    self.entries[row][col].configure(border_color = Config.highlight_duplicate)

    def _grid_complete(self)->bool:
        for col in range(9):
            for row in range(9):
                x=self.entries[row][col].cget("text")
                y=self.solved_array[row][col]
                if x =='':return False
                if int(x) != y:
                    return False
        return True    
    
    def _game_won_event(self):
        a = 2
        ma =  self.master
        while ma.master != None:
            ma = ma.master
        a= 0
        ma.render_new_game()

    def highlight_related(self, event):
        '''the event is not the actual widget
        therefore one cannot perform direct manupulation on the widget
        '''
        widget : SodokuGridButton = event.widget.master
        selected_row = widget.row
        selected_col = widget.col
        self.reset_highlight()
        # Highlight the row
        for col in range(9):
            button : ctk.CTkButton = self.entries[selected_row][col]
            button.configure( border_color=Config.hihglight_in_row_col_box)
        # Highlight the column
        for row in range(9):
            button : ctk.CTkButton = self.entries[row][selected_col]
            button.configure(border_color =Config.hihglight_in_row_col_box)
        # Highlight the 3x3 box
        box_start_row = (selected_row // 3) * 3
        box_start_col = (selected_col // 3) * 3
        for row in range(box_start_row, box_start_row + 3):
            for col in range(box_start_col, box_start_col + 3):
                self.entries[row][col].configure(border_color=Config.hihglight_in_row_col_box)
        # Highlight the selected cell differently
        # and since we cannot perfom direct manupulation on the widget we  refer to it by its row and column
        selected_button = self.entries[selected_row][selected_col]
        selected_button.configure(fg_color=Config.hihglight_in_row_col_box)
    
    def reset_highlight(self ):
        # Reset all cells' background color
        for row in range(9):
            for col in range(9):
                self.entries[row][col].configure(fg_color=Config.default_button_color,border_color="#3E454A")

    def insert_input2(self,event):

        t = threading.Thread(target=self.fill,args=[event.widget.master],daemon=True)
        t.start()
        self.thread.append(t)

    def grid_screenshot(self)->list:
        grid_array = [[self.entries[row][col].cget("text") for col in range(9)]for row in range(9)]
        grid_string = ""
        for row in range(9):
            for col in range(9):
                entry = str(grid_array[row][col])
                if entry == "": entry = " "
                grid_string += entry
        return grid_string
    
    def to_string(array):
        modified = []
        for i  in array:
            if i == "" or i == " ":
                modified.append(0)
            else :
                modified.append(int(i))
        return modified
    
    def create_grid(self):
        arr= 0 
        if self.is_existing:
            arr  =  Config.load_existing_game(level=self.level)
            self.solved_array = Config.load_exsting_solved(level=self.level)
        else : 
            arr =generate(self.level)
            self.solved_array = solved_sodoku(arr)
            
        for row in range(9):
            for col in range(9):
                text = arr.pop(0)
                if text == 0: text = ""
                '''
                entry = ctk.CTkButton(self, width=40,height= 40,fg_color= Config.default_button_color, text=text,font=('Arial', 18), border_width=1,corner_radius=4)
                entry.row = row
                entry.col = col
                entry.grid(row=row, column=col, padx=(2, 2) if col % 3 != 2 else (2, 6), pady=(2, 2) if row % 3 != 2 else (2, 6))
                entry.bind("<Button-1>", self.highlight_related)
                entry.bind("<Button-1>",self.insert_input2)
                '''
                highlight_function = self.highlight_related
                insert_function = self.insert_input2
                self.entries[row][col] = SodokuGridButton(
                    self,
                    text=text,
                    row=row,
                    col=col,
                    higlight_function=highlight_function,
                    insert_function=insert_function
                    )
        
        # Create thicker lines for separating 3x3 grids
        for i in range(1,9):
            if i % 3 == 0:
                self.grid_rowconfigure(i, minsize=10)
                self.grid_columnconfigure(i, minsize=10)
 

        self.highlight_errors()


class SodokuGridButton(ctk.CTkButton):
    def __init__(self,master,text,row,col,higlight_function,insert_function):
        super().__init__(master=master,width=40,height= 40,fg_color= Config.default_button_color, text=text,font=('Arial', 18), border_width=1,corner_radius=4)
        self.row = row
        self.col = col
        self.grid(row=row, column=col, padx=(2, 2) if col % 3 != 2 else (2, 6), pady=(2, 2) if row % 3 != 2 else (2, 6))
        self.bind("<Button-1>", higlight_function)
        self.bind("<Button-1>",insert_function)


        