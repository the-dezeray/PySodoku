from core.file_handler import open_save_file
class Config():
    default_button_text_color = "while"
    default_button_fg_color = "blue"
    default_button_hover_color = "green"
    corner_radius = 2,
    default_button_font_family = 'arial'
    default_button_size  = 3
    default_button_color = "blue"
    default_text_color = "while"
    
    highlight_selected_color : str= "blue"
    highlight_similar: str = "yellow"
    highlight_error_color: str = "red"
    highlight_duplicate : str= "red"
    hihglight_in_row_col_box : str= "yellow"

    default_chapter_label_font_family = ""
    default_chapter_label_font_size = ""
    default_chapter_lable_text_color= ""

    primary_frame_width = 1000
    primary_frame_height = 600
    previous_game_level = "easy"
    
    def load_exisiting_game(level :str = "easy"):
        pass
    def saved_game_exists():
        return 0

    @classmethod
    def load_from_yaml(cls):
        file_data = open_save_file("save.yaml")
        config = file_data["config"]
        for key , value in config.items():
            if hasattr(cls,key):
                setattr(cls,key,value)

    @classmethod
    def capture_gama(cls,grid):
        return 0