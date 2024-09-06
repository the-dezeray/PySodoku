from file_handler import open_save_file,get_save_file,write_to_yaml
class Config():
    default_button_text_color = "#314876"
    default_button_fg_color = "blue"
    default_button_hover_color = "green"
    corner_radius = 2,
    default_button_font_family = 'arial'
    default_button_size  = 3
    default_button_color = "blue"
    default_text_color = "#e3e6eb"
    
    highlight_selected_color : str= "blue"
    highlight_similar: str = "yellow"
    highlight_error_color: str = "red"
    highlight_duplicate : str= "red"
    hihglight_in_row_col_box : str= "yellow"

    default_chapter_label_font_family = ""
    default_chapter_label_font_size = ""
    default_chapter_label_text_color= "#e5f1f4"

    primary_frame_width = 600
    primary_frame_color = "#050707"
    primary_frame_height = 600
    previous_game_level = "easy"
    def load_exsting_solved(level):
        file_data = get_save_file()
        saved_games = file_data["saved_games"]
        solved_grid = saved_games[level]["solved_grid"]
        arr =list(solved_grid)
        kkk =[int(num) for num in arr]
        map = [[None for _ in range(9)] for _ in range(9)]
        for  row in range(9):
            for col in range(9):
                map[row][col] = kkk.pop(0)
        return map
    
    def load_existing_game(level :str = "easy")->list:
        file_data = get_save_file()
        saved_games = file_data["saved_games"]
        grid_string = saved_games[level]["grid"] 
        grid = list(grid_string)
        return grid


    def saved_game_exists(cls,level):
        content = get_save_file()
        level = content["saved_games"][level]
        if level["exists"] == True:
            return True
        else :
            return False

    @classmethod
    def load_from_yaml(cls):
        file_data = get_save_file()
        config = file_data["config"]
        for key , value in config.items():
            if hasattr(cls,key):
                setattr(cls,key,value)

    @classmethod
    def capture_game(cls,grid,level,error_count,time,solved_grid):   
        grid0 = ""
        for row in range(9):
            for col in range(9):
                entry = str(solved_grid[row][col])
                grid0 += entry
        file_content = get_save_file()
        game_entry = file_content["saved_games"][level]
        file_content["saved_games"][level]["grid"] = grid
        file_content["saved_games"][level]["level"] = level
        file_content["saved_games"][level]["error_count"] = error_count
        file_content["saved_games"][level]["time"] = time
        file_content["saved_games"][level]["solved_grid"] = grid0
        # Step 3: Write the updated content back to the YAML file
        write_to_yaml(file_content)
