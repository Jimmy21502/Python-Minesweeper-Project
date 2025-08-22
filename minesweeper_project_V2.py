# Started on 16/07/25
# Version 2
# The goal for Version 2 is to add Minesweeper UI, such as timer, flag counter, etc, and adding tutorial and replayability.

import tkinter as tk
import random as r

# Constants
EASY_GRID = 9
MEDIUM_GRID = 16
GHOSTSWEEPER_GRID = 16
HARD_GRID = 20
FRUIT_GRID = 20
EASY_TOTAL_TILES = 81
MEDIUM_TOTAL_TILES = 256
GHOSTSWEEPER_TOTAL_TILES = 256
HARD_TOTAL_TILES = 400
EASY_TOTAL_BOMBS = 10
MEDIUM_TOTAL_BOMBS = 40
GHOSTSWEEPER_TOTAL_BOMBS = 40
HARD_TOTAL_BOMBS = 80
FRUIT_TOTAL_BOMBS = 20

class Minesweeper:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper Game")

        self.easy_timer_count = None
        self.medium_timer_count = None
        self.hard_timer_count = None
        self.custom_timer_count = None
        self.ghostsweeper_timer_count = None
        self.easy_flag_counter = EASY_TOTAL_BOMBS
        self.medium_flag_counter = MEDIUM_TOTAL_BOMBS
        self.hard_flag_counter = HARD_TOTAL_BOMBS
        self.ghostsweeper_flag_counter = 10
        self.tutorial_counter = 0

        # Container that holds the frames together
        self.container = tk.Frame(self.root)
        self.container.grid(row = 0, column = 0, sticky = "NESW")
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)      
        
        # Dictionary for holding frames created below
        self.frames = {}
        self.frames["PlayFrame"] = self.create_play_frame()
        self.frames["TutorialFrame"] = self.create_tutorial_frame()
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["EasyFrame"] = self.create_easy_frame()
        self.frames["MediumFrame"] = self.create_medium_frame()
        self.frames["HardFrame"] = self.create_hard_frame()
        self.frames["CustomSettingFrame"] = self.create_custom_setting_frame()
        self.frames["GamemodesFrame"] = self.create_gamemodes_frame()
        self.frames["LeaderboardFrame"] = self.create_leaderboard_frame()

        # Shows the Playing Frame first before any other frames
        self.show_frame("PlayFrame")
        
        # Makes the layout responsive e.g. expands proportionally with the window, by changing weight
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)      
        
    def run(self):
        self.root.mainloop()

    # Function to show intended frames by using tkraise which raises a frame to the top of the stack
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

        if name == "EasyFrame":
            self.current_mode = "easy"
        elif name == "MediumFrame":
            self.current_mode = "medium"
        elif name == "HardFrame":
            self.current_mode = "hard"
        elif name == "CustomFrame":
            self.current_mode = "custom"
        else:
            self.current_mode = None

    # Creating the contents displayed for the play frame, repeated for each frame
    def create_play_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        title_label = tk.Label(frame, text="Minesweeper", font="Verdana 22 bold")
        title_label.grid(row = 0, column = 0, columnspan = 2)

        play_button = tk.Button(frame, text="Play", command = lambda: self.show_frame("MainFrame"))
        play_button.grid(row = 1, column = 0, sticky = "NSEW")

        tutorial_button = tk.Button(frame, text="Tutorial", command = lambda: self.show_frame("TutorialFrame"))
        tutorial_button.grid(row = 2, column = 0, sticky = "NSEW")

        for i in range(3):
            frame.grid_rowconfigure(i, weight = 1)
        for j in range(1):
            frame.grid_columnconfigure(j, weight = 1)

        return frame
    
    def create_tutorial_frame(self):
        self.tutorial_frame = tk.Frame(self.container)
        self.tutorial_frame.grid(row = 0, column = 0, sticky = "NSEW")

        self.header_frame = tk.Frame(self.tutorial_frame)
        self.header_frame.grid(row = 0, column = 0, sticky = "EW")

        self.tutorial_label = tk.Label(self.header_frame, text="""Welcome, the goal of Minesweeper is to 
click on every tile that does not contain a bomb. (Click to continue)""")
        self.tutorial_label.grid(row = 0, column = 1, sticky="NSEW", pady=5)
        
        self.header_frame.grid_columnconfigure(0, weight = 1)
        self.header_frame.grid_columnconfigure(2, weight = 1)

        self.grid_frame = tk.Frame(self.tutorial_frame)
        self.grid_frame.grid(row = 1, column = 0, sticky = "NSEW")
        
        self.tutorial_buttons = []

        for i in range(EASY_GRID):
            tutorial_row = []
            for j in range(EASY_GRID):
                tutorial_tile = tk.Button(self.grid_frame, borderwidth=1, width=2, height=1)
                tutorial_tile.grid(row = i, column = j, sticky = "NSEW")
                tutorial_tile.bind('<Button-1>', lambda event, x=i, y=j: self.tutorial_clicks(event, x, y))
                tutorial_tile.bind('<Button-3>', lambda event, x=i, y=j: self.tutorial_clicks(event, x, y))

                tutorial_row.append(tutorial_tile)
            self.tutorial_buttons.append(tutorial_row)
                
        for i in range(EASY_GRID):
            self.grid_frame.grid_rowconfigure(i, weight = 1)
            self.grid_frame.grid_columnconfigure(i, weight = 1)

        self.tutorial_frame.grid_rowconfigure(1, weight = 1)
        self.tutorial_frame.grid_columnconfigure(0, weight = 1)

        return self.tutorial_frame

    def create_main_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        title_label = tk.Label(frame, text="Minesweeper", font="Verdana 22 bold")
        title_label.grid(row = 0, column = 0, columnspan = 2)

        self.easy_button = tk.Button(frame, text="Easy", bg="#86EB83",
                                     font="Verdana 12 bold",
                                     command = lambda: self.show_frame("EasyFrame"))
        self.easy_button.grid(row = 1, column = 0, sticky = "NSEW")

        self.medium_button = tk.Button(frame, text="Medium", bg="#EAFC81",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("MediumFrame"))
        self.medium_button.grid(row = 2, column = 0, sticky = "NSEW")

        self.hard_button = tk.Button(frame, text="Hard", bg="#FF8F74",
                                     font="Verdana 12 bold",
                                     command = lambda: self.show_frame("HardFrame"))
        self.hard_button.grid(row = 3, column = 0, sticky = "NSEW")

        self.custom_button = tk.Button(frame, text="Custom", bg="#EAEAEA",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("CustomSettingFrame"))
        self.custom_button.grid(row = 4, column = 0, sticky = "NSEW")
        
        self.gamemodes_button = tk.Button(frame, text="Gamemodes", bg="#FFD17C",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("GamemodesFrame"))
        self.gamemodes_button.grid(row = 5, column = 0, sticky = "NSEW")

        self.leaderboard_button = tk.Button(frame, text="Leaderboard", bg ="#7CE4FF",
                                            font="Verdana 12 bold",
                                            command = lambda: self.show_frame("LeaderboardFrame"))
        self.leaderboard_button.grid(row = 6, column = 0, sticky = "NSEW")

        for i in range(7):
            frame.grid_rowconfigure(i, weight = 1)
        for j in range(1):
            frame.grid_columnconfigure(j, weight = 1)

        return frame
        
    def create_easy_frame(self):
        self.easy_frame = tk.Frame(self.container)
        self.easy_frame.grid(row = 0, column = 0, sticky = "NSEW")

        self.header_frame = tk.Frame(self.easy_frame)
        self.header_frame.grid(row=0, column=0, sticky = "EW", pady=5)

        self.easy_timer = tk.Label(self.header_frame, text="Timer: 0")
        self.easy_timer.grid(row=0, column=3, padx=5)

        self.easy_reset_game = tk.Button(self.header_frame, text="Reset", command = lambda: [self.reset(EASY_GRID, EASY_GRID, self.easy_buttons, self.easy_bombs, self.easy_flag, EASY_TOTAL_BOMBS), self.stop_timer(self.easy_timer_count)])
        self.easy_reset_game.grid(row=0, column=2, padx=5)

        self.easy_flag = tk.Label(self.header_frame, text="🚩: 10")
        self.easy_flag.grid(row=0, column=0, padx=5)

        self.menu = tk.Button(self.header_frame, text="Menu", command = lambda: [self.show_frame("MainFrame"), self.reset(EASY_GRID, EASY_GRID, self.easy_buttons, self.easy_bombs, self.easy_flag, EASY_TOTAL_BOMBS), self.stop_timer(self.easy_timer_count)])
        self.menu.grid(row=0, column=5, padx=5)
        
        self.header_frame.grid_columnconfigure(1, weight = 1)
        self.header_frame.grid_columnconfigure(4, weight = 1)

        self.grid_frame = tk.Frame(self.easy_frame)
        self.grid_frame.grid(row=1, column=0, sticky = "NSEW")

        # List for storing the buttons themselves and empty bomb list as the bombs should be generated after the first click
        self.easy_buttons = []
        self.easy_bombs = []

        # Creating 9x9 tiles
        for i in range(EASY_GRID):
            # Creating 9 rows
            easy_row = []
            for j in range(EASY_GRID):
                easy_tile = tk.Button(self.grid_frame, borderwidth=1, width=2, height=1)
                easy_tile.grid(row = i, column = j, sticky = "NSEW")

                # Binding each tile to left and right click, and passing an event which can be anything but is required
                easy_tile.bind('<Button-1>', lambda event, x=i, y=j: self.left_click(self.easy_clicks, x, y, EASY_GRID, EASY_GRID, self.easy_buttons, EASY_TOTAL_TILES, EASY_TOTAL_BOMBS, self.easy_timer_count))
                easy_tile.bind('<Button-3>', lambda event, x=i, y=j: self.right_click(x, y, self.easy_buttons))
                
                # Appends 9 columns to the 9 rows, giving the 81 intended buttons 
                easy_row.append(easy_tile)
            self.easy_buttons.append(easy_row)

        for i in range(EASY_GRID):
            self.grid_frame.grid_rowconfigure(i, weight = 1)
            self.grid_frame.grid_columnconfigure(i, weight = 1)

        self.easy_frame.grid_rowconfigure(1, weight = 1)
        self.easy_frame.grid_columnconfigure(0, weight = 1)

        return self.easy_frame

    def create_medium_frame(self):
        self.medium_frame = tk.Frame(self.container)
        self.medium_frame.grid(row=0, column=0, sticky = "NSEW")

        self.header_frame = tk.Frame(self.medium_frame)
        self.header_frame.grid(row=0, column=0, sticky = "EW", pady=5)

        self.medium_timer = tk.Label(self.header_frame, text="Timer: 0")
        self.medium_timer.grid(row=0, column=3, padx=5)

        self.medium_reset_game = tk.Button(self.header_frame, text="Reset", command = lambda: [self.reset(MEDIUM_GRID, MEDIUM_GRID, self.medium_buttons, self.medium_bombs, self.medium_flag, MEDIUM_TOTAL_BOMBS), self.stop_timer(self.medium_timer_count)])
        self.medium_reset_game.grid(row=0, column=2, padx=5)

        self.medium_flag = tk.Label(self.header_frame, text="🚩: 40")
        self.medium_flag.grid(row=0, column=0, sticky="W", padx=5)

        self.menu = tk.Button(self.header_frame, text="Menu", command = lambda: [self.show_frame("MainFrame"), self.reset(MEDIUM_GRID, MEDIUM_GRID, self.medium_buttons, self.medium_bombs, self.medium_flag, MEDIUM_TOTAL_BOMBS), self.stop_timer(self.medium_timer_count)])
        self.menu.grid(row=0, column=5, sticky="E", padx=5)
        
        self.header_frame.grid_columnconfigure(1, weight = 1)
        self.header_frame.grid_columnconfigure(4, weight = 1)

        self.grid_frame = tk.Frame(self.medium_frame)
        self.grid_frame.grid(row=1, column=0, sticky = "NSEW")

        self.medium_buttons = []
        self.medium_bombs = []

        for i in range(MEDIUM_GRID):
            medium_row = []
            for j in range(MEDIUM_GRID):
                medium_tile = tk.Button(self.grid_frame, borderwidth=1, width=2, height=1)
                medium_tile.grid(row = i, column = j, sticky = "NSEW")
                medium_tile.bind('<Button-1>', lambda event, x=i, y=j: self.left_click(self.medium_clicks, x, y, MEDIUM_GRID, MEDIUM_GRID, self.medium_buttons, MEDIUM_TOTAL_TILES, MEDIUM_TOTAL_BOMBS, self.medium_timer_count))
                medium_tile.bind('<Button-3>', lambda event, x=i, y=j: self.right_click(x, y, self.medium_buttons))
                medium_row.append(medium_tile)
            self.medium_buttons.append(medium_row)

        for i in range(MEDIUM_GRID):
            self.grid_frame.grid_rowconfigure(i, weight = 1)
            self.grid_frame.grid_columnconfigure(i, weight = 1)
    
        self.medium_frame.grid_rowconfigure(1, weight = 1)
        self.medium_frame.grid_columnconfigure(0, weight = 1)

        return self.medium_frame

    def create_hard_frame(self):
        self.hard_frame = tk.Frame(self.container)
        self.hard_frame.grid(row = 0, column = 0, sticky = "NSEW")

        self.header_frame = tk.Frame(self.hard_frame)
        self.header_frame.grid(row=0, column=0, sticky = "EW", pady=5)

        self.hard_timer = tk.Label(self.header_frame, text="Timer: 0")
        self.hard_timer.grid(row=0, column=3, padx=5)

        self.hard_reset_game = tk.Button(self.header_frame, text="Reset", command = lambda: [self.reset(HARD_GRID, HARD_GRID, self.hard_buttons, self.hard_bombs, self.hard_flag, HARD_TOTAL_BOMBS), self.stop_timer(self.hard_timer_count)])
        self.hard_reset_game.grid(row=0, column=2, padx=5)

        self.hard_flag = tk.Label(self.header_frame, text="🚩: 80")
        self.hard_flag.grid(row=0, column=0, padx=5)

        self.menu = tk.Button(self.header_frame, text="Menu", command = lambda: [self.show_frame("MainFrame"), self.reset(HARD_GRID, HARD_GRID, self.hard_buttons, self.hard_bombs, self.hard_flag, HARD_TOTAL_BOMBS), self.stop_timer(self.hard_timer_count)])
        self.menu.grid(row=0, column=5, padx=5)

        self.header_frame.grid_columnconfigure(1, weight = 1)
        self.header_frame.grid_columnconfigure(4, weight = 1)

        self.grid_frame = tk.Frame(self.hard_frame)
        self.grid_frame.grid(row=1, column=0, sticky = "NSEW")

        self.hard_buttons = []
        self.hard_bombs = []

        for i in range(HARD_GRID):
            hard_row = []
            for j in range(HARD_GRID):
                hard_tile = tk.Button(self.grid_frame, borderwidth=1, width=2, height=1)
                hard_tile.grid(row = i, column = j, sticky = "NSEW")
                hard_tile.bind('<Button-1>', lambda event, x=i, y=j: self.left_click(self.hard_clicks, x, y, HARD_GRID, HARD_GRID, self.hard_buttons, HARD_TOTAL_TILES, HARD_TOTAL_BOMBS, self.hard_timer_count))
                hard_tile.bind('<Button-3>', lambda event, x=i, y=j: self.right_click(x, y, self.hard_buttons))
                hard_row.append(hard_tile)
            self.hard_buttons.append(hard_row)

        for i in range(HARD_GRID):
            self.grid_frame.grid_rowconfigure(i, weight = 1)
            self.grid_frame.grid_columnconfigure(i, weight = 1)

        self.hard_frame.grid_rowconfigure(1, weight = 1)
        self.hard_frame.grid_columnconfigure(0, weight = 1)

        return self.hard_frame

    def create_custom_setting_frame(self):
        self.custom_setting_frame = tk.Frame(self.container)
        self.custom_setting_frame.grid(row=0, column=0, sticky = "NSEW")

        self.rows_label = tk.Label(self.custom_setting_frame, text="Rows (8 min / 20 max): ")
        self.rows_label.grid(row=0, column=0)
        self.row_entry = tk.Entry(self.custom_setting_frame)
        self.row_entry.grid(row=0, column=1)

        self.columns_label = tk.Label(self.custom_setting_frame, text="Columns (8 min / 32 max): ")
        self.columns_label.grid(row=1, column=0)
        self.column_entry = tk.Entry(self.custom_setting_frame)
        self.column_entry.grid(row=1, column=1)

        self.bombs_label = tk.Label(self.custom_setting_frame, text="Bombs: ")
        self.bombs_label.grid(row=2, column=0)
        self.bomb_entry = tk.Entry(self.custom_setting_frame)
        self.bomb_entry.grid(row=2, column=1)

        self.start_button = tk.Button(self.custom_setting_frame, text="Start Game", command = self.create_custom_frame)
        self.start_button.grid(row=3, column=0, columnspan=2)

        self.return_button = tk.Button(self.custom_setting_frame, text="Return", command = lambda: self.show_frame("MainFrame"))
        self.return_button.grid(row=4, column=0, columnspan=2)

        return self.custom_setting_frame

    def create_custom_frame(self):
        try:
            self.custom_rows = int(self.row_entry.get())
            self.custom_columns = int(self.column_entry.get())
            self.custom_total_bombs = int(self.bomb_entry.get())
            self.custom_flag_counter = self.custom_total_bombs

        except ValueError:
            return
        
        if self.custom_rows < 8 or self.custom_rows > 20 or self.custom_columns < 8 or self.custom_columns > 32:
            return
        
        if self.custom_total_bombs > int((self.custom_rows*self.custom_columns)/(10/3)) or self.custom_total_bombs < 10:
            self.bombs_label.config(text=f"Bombs: (10 min / {str((self.custom_rows*self.custom_columns)/(10/3))} max):")
            return
        
        self.custom_frame = tk.Frame(self.container)
        self.custom_frame.grid(row=0, column=0, sticky = "NSEW")

        self.header_frame = tk.Frame(self.custom_frame)
        self.header_frame.grid(row=0, column=0, sticky = "EW", pady=5)

        self.custom_timer = tk.Label(self.header_frame, text="Timer: 0")
        self.custom_timer.grid(row=0, column=3, padx=5)

        self.custom_reset_game = tk.Button(self.header_frame, text="Reset", command = lambda: [self.reset(self.custom_rows, self.custom_columns, self.custom_buttons, self.custom_bombs, self.custom_flag, self.custom_total_bombs), self.stop_timer(self.custom_timer_count)])
        self.custom_reset_game.grid(row=0, column=2, padx=5)

        self.custom_flag = tk.Label(self.header_frame, text=f"🚩: {self.custom_total_bombs}")
        self.custom_flag.grid(row=0, column=0, padx=5)

        self.menu = tk.Button(self.header_frame, text="Menu", command = lambda: [self.show_frame("MainFrame"), self.reset(HARD_GRID, HARD_GRID, self.hard_buttons, self.hard_bombs, self.hard_flag, HARD_TOTAL_BOMBS), self.stop_timer(self.hard_timer_count)])
        self.menu.grid(row=0, column=5, padx=5)

        self.header_frame.grid_columnconfigure(1, weight = 1)
        self.header_frame.grid_columnconfigure(4, weight = 1)

        self.grid_frame = tk.Frame(self.custom_frame)
        self.grid_frame.grid(row=1, column=0, sticky = "NSEW")

        self.custom_buttons = []
        self.custom_bombs = []

        for i in range(self.custom_rows):
            custom_row = []
            for j in range(self.custom_columns):
                custom_tile = tk.Button(self.grid_frame, borderwidth=1, width=2, height=1)
                custom_tile.grid(row = i, column = j, sticky = "NSEW")
                custom_tile.bind('<Button-1>', lambda event, x=i, y=j: self.left_click(self.custom_clicks, x, y, self.custom_rows, self.custom_columns, self.custom_buttons, (self.custom_columns*self.custom_rows), self.custom_total_bombs, self.custom_timer_count))
                custom_tile.bind('<Button-3>', lambda event, x=i, y=j: self.right_click(x, y, self.custom_buttons))
                custom_row.append(custom_tile)
            self.custom_buttons.append(custom_row)
        
        for i in range(self.custom_rows):
            self.grid_frame.grid_rowconfigure(i, weight = 1)
        for j in range(self.custom_columns):
            self.grid_frame.grid_columnconfigure(j, weight = 1)

        self.custom_frame.grid_rowconfigure(1, weight = 1)
        self.custom_frame.grid_columnconfigure(0, weight = 1)

        return self.custom_frame
    
    # WIP
    def create_gamemodes_frame(self):
        self.gamemodes_frame = tk.Frame(self.container)
        self.gamemodes_frame.grid(row=0, column=0, sticky = "NSEW")

        self.gamemode_one_frame = tk.Button(self.gamemodes_frame, text="Gamemode 1: Fruitsweeper", command = self.create_fruitsweeper_frame)
        self.gamemode_one_frame.grid(row=0, column=0, sticky = "NSEW")

        self.gamemode_one_info_frame = tk.Button(self.gamemodes_frame, text="Info", command = self.create_fruitsweeper_info_frame)
        self.gamemode_one_info_frame.grid(row=0, column=1, sticky = "NSEW")

        self.gamemode_two_frame = tk.Button(self.gamemodes_frame, text="Gamemode 2: Ghostsweeper", command = self.create_ghostsweeper_frame)
        self.gamemode_two_frame.grid(row=1, column=0, sticky = "NSEW")
        
        self.gamemode_two_frame = tk.Button(self.gamemodes_frame, text="Info", command = self.create_ghostsweeper_info_frame)
        self.gamemode_two_frame.grid(row=1, column=1, sticky = "NSEW")

        self.menu_button = tk.Button(self.gamemodes_frame, text="Back to Menu", command = lambda: self.show_frame("MainFrame"))
        self.menu_button.grid(row=2, column=0, sticky="SEW")

        return self.gamemodes_frame

    def create_fruitsweeper_frame(self):
        self.fruit_sweeper_frame = tk.Frame(self.container)
        self.fruit_sweeper_frame.grid(row = 0, column = 0, sticky = "NSEW")

        self.header_frame = tk.Frame(self.fruit_sweeper_frame)
        self.header_frame.grid(row=0, column=0, sticky = "EW", pady=5)

        self.bomb_count = tk.Label(self.header_frame, text="Bombs: 20")
        self.bomb_count.grid(row=0, column=3, padx=5)

        self.fruit_reset_game = tk.Button(self.header_frame, text="Reset", command = self.create_fruitsweeper_frame)
        self.fruit_reset_game.grid(row=0, column=2, padx=5)

        self.points = tk.Label(self.header_frame, text="0")
        self.points.grid(row=0, column=0, padx=5)

        self.menu = tk.Button(self.header_frame, text="Menu", command = lambda: self.show_frame("MainFrame"))
        self.menu.grid(row=0, column=5, padx=5)

        self.header_frame.grid_columnconfigure(1, weight = 1)
        self.header_frame.grid_columnconfigure(4, weight = 1)

        self.grid_frame = tk.Frame(self.fruit_sweeper_frame)
        self.grid_frame.grid(row=1, column=0, sticky = "NSEW")

        self.fruit_buttons = []
        self.fruit_bombs = 20

        for i in range(FRUIT_GRID):
            fruit_row = []
            for j in range(FRUIT_GRID):
                fruit_tile = tk.Button(self.grid_frame, borderwidth=1, width=2, height=1)
                fruit_tile.grid(row = i, column = j, sticky = "NSEW")
                fruit_tile.bind('<Button-1>', lambda event, x=i, y=j: self.fruit_clicks(x, y))
                fruit_row.append(fruit_tile)
            self.fruit_buttons.append(fruit_row)

        self.fruits = [
            {"name" : "🍎", "value" : 10},
            {"name" : "🍌", "value" : 25},
            {"name" : "🍇", "value" : 35},
            {"name" : "🍍", "value" : 50},
            {"name" : "🍓", "value" : 100},
            {"name" : "🫐", "value" : 110},
            {"name" : "🍋", "value" : -50},
            {"name" : "👑", "value" : 250},
            {"name" : "💎", "value" : 500},
            {"name" : "⚠️", "value" : 0},
            {"name" : "💣", "value" : 0}
            ]
            
        self.fruitsweeper_tile_locations = [(i, j) for i  in range(FRUIT_GRID) for j in range(FRUIT_GRID)]
        self.fruit_tile_locations = r.sample(self.fruitsweeper_tile_locations, k=120)

        for (x, y) in self.fruitsweeper_tile_locations:
            button = self.fruit_buttons[x][y]
            if (x, y) in self.fruit_tile_locations:
                fruit = r.choices(self.fruits, weights=(16, 25, 20, 15, 4, 5, 5, 3, 2, 1, 4), k=1)[0]
                button.fruit = fruit
            else:
                button.fruit = None
        
        for i in range(FRUIT_GRID):
            self.grid_frame.grid_rowconfigure(i, weight = 1)
            self.grid_frame.grid_columnconfigure(i, weight = 1)

        self.fruit_sweeper_frame.grid_rowconfigure(1, weight = 1)
        self.fruit_sweeper_frame.grid_columnconfigure(0, weight = 1)

        return self.fruit_sweeper_frame
    
    def fruit_clicks(self, i, j):
        self.surrounding_tiles = (i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)

        if self.fruit_buttons[i][j]["state"] == "disabled":
            return

        for (i, j) in self.surrounding_tiles:
            if i < 0 or i > (FRUIT_GRID-1) or j < 0 or j > (FRUIT_GRID-1):
                continue

            button = self.fruit_buttons[i][j]

            if button["state"] == "disabled":
                continue
            
            if button.fruit is None:
                button.config(text="", bg = "light grey", state="disabled")
            else:
                button.config(text=button.fruit["name"], bg = "light green", state="disabled")
                current_points = int(self.points["text"])
                self.points.config(text=(current_points + button.fruit["value"]))
                if button.fruit["name"] == "⚠️" and not self.fruit_bombs == 0:
                    for i in range(FRUIT_GRID):
                        for j in range(FRUIT_GRID):
                            self.fruit_buttons[i][j].config(state="disabled", bg="red")
                if button.fruit["name"] == "💣":
                    self.fruit_bombs += 1

        self.fruit_bombs -= 1
        self.bomb_count.config(text=f"Bombs: {self.fruit_bombs}")

        if self.fruit_bombs == 0:
            for i in range(FRUIT_GRID):
                for j in range(FRUIT_GRID):
                    self.fruit_buttons[i][j].config(state="disabled", bg="light green")

    def create_fruitsweeper_info_frame(self):
        self.fruitsweeper_info_frame = tk.Frame(self.container)
        self.fruitsweeper_info_frame.grid(row=0, column=0, sticky="NSEW")

        self.title_label = tk.Label(self.fruitsweeper_info_frame, text="Fruitsweeper", font="Arial 20 bold")
        self.title_label.grid(row=0, column=0, columnspan=2, sticky = "NEW", pady=15)

        self.info_label = tk.Label(self.fruitsweeper_info_frame, text="""Welcome to Fruitsweeper!
The objective of this gamemode is to score the highest amount of points possible.
In this gamemode, you use 20 bombs to reveal tiles in a 3x3 radius where clicked.
Each tile revealed has a chance of being a fruit (or other items), granting points.
The game ends when you use up all 20 bombs, so use them wisely!
NOTE: This gamemode is completely luck based.

For your reference:
🍎: 10 Points
🍌: 25 Points
🍇: 35 Points
🍍: 50 Points
🍓: 100 Points
🫐: 110 Points
🍋: -50 Points
👑: 250 Points
💎: 500 Points
⚠️: Ends the game immediately
💣: Gives you one bomb""")
        self.info_label.grid(row=1, column=0, sticky="NSEW", pady=30)

        self.info_return_button = tk.Button(self.fruitsweeper_info_frame, text="Return", command= lambda: self.show_frame("GamemodesFrame"))
        self.info_return_button.grid(row=2, column=0, sticky="SEW")

        self.fruitsweeper_info_frame.grid_rowconfigure(2, weight = 1)
        self.fruitsweeper_info_frame.grid_columnconfigure(0, weight = 1)      

        return self.fruitsweeper_info_frame

    def create_ghostsweeper_frame(self):
        self.ghostsweeper_frame = tk.Frame(self.container)
        self.ghostsweeper_frame.grid(row=0, column=0, sticky = "NSEW")

        self.header_frame = tk.Frame(self.ghostsweeper_frame)
        self.header_frame.grid(row=0, column=0, sticky = "EW", pady=5)

        self.ghostsweeper_timer = tk.Label(self.header_frame, text="Timer: 300")
        self.ghostsweeper_timer.grid(row=0, column=3, padx=5)

        self.ghostsweeper_reset_game = tk.Button(self.header_frame, text="Reset", command = lambda: [self.reset(GHOSTSWEEPER_GRID, GHOSTSWEEPER_GRID, self.ghostsweeper_buttons, self.ghostsweeper_bombs, self.ghostsweeper_flag, GHOSTSWEEPER_TOTAL_BOMBS), self.stop_timer(self.ghostsweeper_timer_count)])
        self.ghostsweeper_reset_game.grid(row=0, column=2, padx=5)

        self.ghostsweeper_flag = tk.Label(self.header_frame, text="💡: 10")
        self.ghostsweeper_flag.grid(row=0, column=0, padx=5)

        self.menu = tk.Button(self.header_frame, text="Menu", command = lambda: [self.show_frame("MainFrame"), self.reset(GHOSTSWEEPER_GRID, GHOSTSWEEPER_GRID, self.ghostsweeper_buttons, self.ghostsweeper_bombs, self.ghostsweeper_flag, GHOSTSWEEPER_TOTAL_BOMBS), self.stop_timer(self.ghostsweeper_timer_count)])
        self.menu.grid(row=0, column=5, padx=5)
        
        self.header_frame.grid_columnconfigure(1, weight = 1)
        self.header_frame.grid_columnconfigure(4, weight = 1)

        self.grid_frame = tk.Frame(self.ghostsweeper_frame)
        self.grid_frame.grid(row=1, column=0, sticky = "NSEW")

        self.ghostsweeper_buttons = []
        self.ghostsweeper_bombs = []

        for i in range(GHOSTSWEEPER_GRID):
            ghostsweeper_row = []
            for j in range(GHOSTSWEEPER_GRID):
                ghostsweeper_tile = tk.Button(self.grid_frame, borderwidth=1, width=2, height=1)
                ghostsweeper_tile.grid(row = i, column = j, sticky = "NSEW")
                ghostsweeper_tile.bind('<Button-1>', lambda event, x=i, y=j: self.left_click(self.ghostsweeper_clicks, x, y, GHOSTSWEEPER_GRID, GHOSTSWEEPER_GRID, self.ghostsweeper_buttons, GHOSTSWEEPER_TOTAL_TILES, GHOSTSWEEPER_TOTAL_BOMBS, self.ghostsweeper_timer_count))
                ghostsweeper_tile.bind('<Button-3>', lambda event, x=i, y=j: self.right_click(x, y, self.ghostsweeper_buttons))
                ghostsweeper_row.append(ghostsweeper_tile)
            self.ghostsweeper_buttons.append(ghostsweeper_row)

        for i in range(GHOSTSWEEPER_GRID):
            self.grid_frame.grid_rowconfigure(i, weight = 1)
            self.grid_frame.grid_columnconfigure(i, weight = 1)
    
        self.ghostsweeper_frame.grid_rowconfigure(1, weight = 1)
        self.ghostsweeper_frame.grid_columnconfigure(0, weight = 1)

        return self.ghostsweeper_frame
    
    def ghostsweeper_clicks(self, i, j):
        self.current_mode = "ghostsweeper"
        if self.ghostsweeper_buttons[i][j]["text"] == "💡":
            return
        if self.ghostsweeper_buttons[i][j]["bg"] == "red":
            return
        if self.ghostsweeper_buttons[i][j]["bg"] == "black":
            return

        if len(self.ghostsweeper_bombs) == 0:
            self.start_timer()
            self.ghostsweeper_tile_locations = [(i, j) for i  in range(GHOSTSWEEPER_GRID) for j in range(GHOSTSWEEPER_GRID)]
            self.surrounding_tiles = (i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)
            ghostsweeper_excluded_tiles = []
            for x, y in self.surrounding_tiles:
                if 0 <= x < GHOSTSWEEPER_GRID and 0 <= y < GHOSTSWEEPER_GRID:
                    ghostsweeper_excluded_tiles.append((x, y))
            ghostsweeper_safe_tiles = []
            for tile in self.ghostsweeper_tile_locations:
                if tile not in ghostsweeper_excluded_tiles:
                    ghostsweeper_safe_tiles.append(tile)
            self.ghostsweeper_bombs = r.sample(ghostsweeper_safe_tiles, k=GHOSTSWEEPER_TOTAL_BOMBS)

        lit_tiles = []

        print(f"You clicked: ({i}, {j})") # For Debugging
        if (i, j) in self.ghostsweeper_bombs and not self.ghostsweeper_buttons[i][j]["state"] == "disabled":
            self.stop_timer(self.ghostsweeper_timer_count)
            print("Bomb")
            for (i, j) in self.ghostsweeper_bombs:
                self.ghostsweeper_buttons[i][j].config(text="👻")
            for (i, j) in self.ghostsweeper_tile_locations:
                self.ghostsweeper_buttons[i][j].config(bg="red", state="disabled")
        else:
            print("Safe")
            self.reveal_tiles(i, j, self.ghostsweeper_bombs, self.ghostsweeper_buttons, GHOSTSWEEPER_GRID, GHOSTSWEEPER_GRID)

            for i in range(GHOSTSWEEPER_GRID):
                for j in range(GHOSTSWEEPER_GRID):
                    if self.ghostsweeper_buttons[i][j]["bg"] == "light grey" or self.ghostsweeper_buttons[i][j]["text"] == "💡":
                        lit_tiles.append((i, j))

            extra_tiles = []
            for x, y in lit_tiles:
                surrounding = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
                for nx, ny in surrounding:
                    if 0 <= nx < GHOSTSWEEPER_GRID and 0 <= ny < GHOSTSWEEPER_GRID:
                        if (nx, ny) not in extra_tiles:
                            extra_tiles.append((nx, ny))
            lit_tiles.extend(extra_tiles)

            for i in range(GHOSTSWEEPER_GRID):
                for j in range(GHOSTSWEEPER_GRID):
                    if (i, j) not in lit_tiles:
                        self.ghostsweeper_buttons[i][j].config(bg="black", state="disabled")
                    else:
                        if self.ghostsweeper_buttons[i][j]["bg"] != "light grey":
                            self.ghostsweeper_buttons[i][j].config(bg="SystemButtonFace", state="normal")

    def create_ghostsweeper_info_frame(self):
        self.ghostsweeper_info_frame = tk.Frame(self.container)
        self.ghostsweeper_info_frame.grid(row=0, column=0, sticky="NSEW")

        self.title_label = tk.Label(self.ghostsweeper_info_frame, text="Ghostsweeper", font="Arial 20 bold")
        self.title_label.grid(row=0, column=0, columnspan=2, sticky = "NEW", pady=15)

        self.info_label = tk.Label(self.ghostsweeper_info_frame, text="""Welcome to Ghostsweeper!
The objective of this gamemode is to reveal the entire haunted grid 
before the time runs out. Using limited lights to illuminate tiles, 
you must avoid hidden ghosts, as clicking a ghost ends the game immediately.
Lit tiles reveal tiles the same as regular tiles, but you only have 10.
This leaves you with fewer lights to navigate the haunted grid.
Use your lights sparingly, and reveal every tile to win!""")
        self.info_label.grid(row=1, column=0, sticky="NSEW", pady=30)

        self.info_return_button = tk.Button(self.ghostsweeper_info_frame, text="Return", command= lambda: self.show_frame("GamemodesFrame"))
        self.info_return_button.grid(row=2, column=0, sticky="SEW")

        self.ghostsweeper_info_frame.grid_rowconfigure(2, weight = 1)
        self.ghostsweeper_info_frame.grid_columnconfigure(0, weight = 1)      

        return self.ghostsweeper_info_frame

    # WIP
    def create_leaderboard_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        return frame

    # This function controls when to move onto the next instruction during the tutorial.
    def tutorial_clicks(self, event, i, j):
        # self.tutorial_counter starts with a value of 0, increasing by 1 to indicate moving onto the next part of the tutorial.
        # event.num represents mouse actions, with 1 being left-clicks and 3 being right-clicks.
        if self.tutorial_counter == 7 and event.num == 1:
            self.show_frame("EasyFrame")

        if self.tutorial_counter == 6 and event.num == 1:
            self.tutorial_label.config(text="""Now that you've got the basics down, you are ready to attempt the real game.
(Click to continue)""")
            self.tutorial_counter = 7

        if i == 1 and j == 7 and event.num == 3 and self.tutorial_counter == 5:
            self.tutorial_buttons[i][j].config(bg="SystemButtonFace")
            self.tutorial_buttons[0][8].config(bg="light grey")
            self.tutorial_buttons[i][j].config(text="🚩")
            self.tutorial_buttons[0][6].config(bg="light green")
            self.tutorial_buttons[1][6].config(bg="light green")
            self.tutorial_buttons[2][8].config(bg="light green")
            self.tutorial_buttons[2][7].config(bg="light green")
            self.tutorial_label.config(text="""The green tiles must be safe to reveal because the tiles numbered 1 are already 
touching a bomb, so the surrounding tiles must be safe. (Click to continue)""")
            self.tutorial_counter = 6
            
        if event.num == 1 and self.tutorial_counter == 4:
            self.tutorial_label.config(text="""You should flag tiles which you think are bombs, flags can be used to 
keep track of where bombs are. Try right-clicking on the red tile to place a flag.""")
            self.tutorial_counter = 5

        if event.num == 1 and self.tutorial_counter == 3:
            for i in range(EASY_GRID):
                for j in range(EASY_GRID):
                    self.tutorial_buttons[i][j].config(bg="SystemButtonFace", text="")
            self.tutorial_buttons[0][8].config(text="1", bg="light green")
            self.tutorial_buttons[0][7].config(text="1", bg="light grey")
            self.tutorial_buttons[1][8].config(text="1", bg="light grey")
            self.tutorial_buttons[1][7].config(bg="red")
            self.tutorial_label.config(text="""In this scenario, the green tile is touching one bomb. It is also only touching 
one tile, therefore the tile highlighted red must be a bomb. (Click to continue)""")
            self.tutorial_counter = 4

        if event.num == 1 and self.tutorial_counter == 2:
            for x, y in self.neighboring_tiles:
                self.tutorial_buttons[x][y].config(bg="red")
            self.tutorial_label.config(text="""Therefore, one of these tiles highlighted red must be a bomb.
(Click to continue)""")
            self.tutorial_counter = 3
                
        if i == 4 and j == 4 and self.tutorial_counter == 1 and event.num == 1:
            self.tutorial_buttons[i][j].config(text="1")
            self.tutorial_label.config(text="""The number on the tile represents the number of bombs surrounding that tile.
(Click to continue)""")
            self.neighboring_tiles = (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)
            self.tutorial_counter = 2

        if event.num == 1 and self.tutorial_counter == 0:
            self.tutorial_buttons[4][4].config(bg="light green")
            self.tutorial_label.config(text="""Try revealing a tile. 
(Click on the tile highlighted green to continue)""")
            self.tutorial_counter = 1

    def easy_clicks(self, i, j):
        # If the tile if flagged, user cannot reveal it until it is unflagged
        if self.easy_buttons[i][j]["text"] == "🚩":
            return
        # It will be the first click if the bombs list is empty
        if len(self.easy_bombs) == 0:
            self.start_timer()
            # Creates location for each tile, frim (0, 0) to (8, 8), and creating the tiles that excludes where the bombs can be generated
            self.easy_tile_locations = [(i, j) for i  in range(EASY_GRID) for j in range(EASY_GRID)]
            self.surrounding_tiles = (i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)
            easy_excluded_tiles = []
            for x, y in self.surrounding_tiles:
                if 0 <= x < EASY_GRID and 0 <= y < EASY_GRID:
                    easy_excluded_tiles.append((x, y))
            # Checking surrounding tiles, and if it is within bounds it will be appended to the excluded tiles. The safe tiles are every tile except the excluded tiles
            easy_safe_tiles = []
            for tile in self.easy_tile_locations:
                if tile not in easy_excluded_tiles:
                    easy_safe_tiles.append(tile)
            # Generating bombs from safe tiles, where k is equal to the number of bombs generated
            self.easy_bombs = r.sample(easy_safe_tiles, k=EASY_TOTAL_BOMBS)

        print(f"You clicked: ({i}, {j})") # For Debugging
        if (i, j) in self.easy_bombs and not self.easy_buttons[i][j]["state"] == "disabled":
            self.stop_timer(self.easy_timer_count)
            print("Bomb")
            for (i, j) in self.easy_bombs:
                self.easy_buttons[i][j].config(text="💣")
            for (i, j) in self.easy_tile_locations:
                self.easy_buttons[i][j].config(bg="red", state="disabled")
        else:
            print("Safe")
            self.reveal_tiles(i, j, self.easy_bombs, self.easy_buttons, EASY_GRID, EASY_GRID)

    def medium_clicks(self, i, j):
        if self.medium_buttons[i][j]["text"] == "🚩":
            return
        if len(self.medium_bombs) == 0:
            self.start_timer()
            self.medium_tile_locations = [(i, j) for i  in range(MEDIUM_GRID) for j in range(MEDIUM_GRID)]
            self.surrounding_tiles = (i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)
            medium_excluded_tiles = []
            for x, y in self.surrounding_tiles:
                if 0 <= x < MEDIUM_GRID and 0 <= y < MEDIUM_GRID:
                    medium_excluded_tiles.append((x, y))
            medium_safe_tiles = []
            for tile in self.medium_tile_locations:
                if tile not in medium_excluded_tiles:
                    medium_safe_tiles.append(tile)
            self.medium_bombs = r.sample(medium_safe_tiles, k=MEDIUM_TOTAL_BOMBS)

        print(f"You clicked: ({i}, {j})") # For Debugging
        if (i, j) in self.medium_bombs and not self.medium_buttons[i][j]["state"] == "disabled":
            self.stop_timer(self.medium_timer_count)
            print("Bomb")
            for (i, j) in self.medium_bombs:
                self.medium_buttons[i][j].config(text="💣")
            for (i, j) in self.medium_tile_locations:
                self.medium_buttons[i][j].config(bg="red", state="disabled")
        else:
            print("Safe")
            self.reveal_tiles(i, j, self.medium_bombs, self.medium_buttons, MEDIUM_GRID, MEDIUM_GRID)

    def hard_clicks(self, i, j):
        if self.hard_buttons[i][j]["text"] == "🚩":
            return
        if len(self.hard_bombs) == 0:
            self.start_timer()
            self.hard_tile_locations = [(i, j) for i  in range(HARD_GRID) for j in range(HARD_GRID)]
            self.surrounding_tiles = (i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)
            hard_excluded_tiles = []
            for x, y in self.surrounding_tiles:
                if 0 <= x < HARD_GRID and 0 <= y < HARD_GRID:
                    hard_excluded_tiles.append((x, y))
            hard_safe_tiles = []
            for tile in self.hard_tile_locations:
                if tile not in hard_excluded_tiles:
                    hard_safe_tiles.append(tile)
            self.hard_bombs = r.sample(hard_safe_tiles, k=HARD_TOTAL_BOMBS)

        print(f"You clicked: ({i}, {j})") # For Debugging
        if (i, j) in self.hard_bombs and not self.hard_buttons[i][j]["state"] == "disabled":
            self.stop_timer(self.hard_timer_count)
            print("Bomb")
            for (i, j) in self.hard_bombs:
                self.hard_buttons[i][j].config(text="💣")
            for (i, j) in self.hard_tile_locations:
                self.hard_buttons[i][j].config(bg="red", state="disabled")
        else:
            print("Safe")
            self.reveal_tiles(i, j, self.hard_bombs, self.hard_buttons, HARD_GRID, HARD_GRID)

    
    def custom_clicks(self, i, j):
        self.current_mode = "custom"
        if self.custom_buttons[i][j]["text"] == "🚩":
            return
        if len(self.custom_bombs) == 0:
            self.start_timer()
            self.custom_tile_locations = [(i, j) for i  in range(self.custom_rows) for j in range(self.custom_columns)]
            self.surrounding_tiles = (i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)
            custom_excluded_tiles = []
            for x, y in self.surrounding_tiles:
                if 0 <= x < self.custom_rows and 0 <= y < self.custom_columns:
                    custom_excluded_tiles.append((x, y))
            custom_safe_tiles = []
            for tile in self.custom_tile_locations:
                if tile not in custom_excluded_tiles:
                    custom_safe_tiles.append(tile)
            self.custom_bombs = r.sample(custom_safe_tiles, k=self.custom_total_bombs)

        print(f"You clicked: ({i}, {j})") # For Debugging
        if (i, j) in self.custom_bombs and not self.custom_buttons[i][j]["state"] == "disabled":
            self.stop_timer(self.custom_timer_count)
            print("Bomb")
            for (i, j) in self.custom_bombs:
                self.custom_buttons[i][j].config(text="💣")
            for (i, j) in self.custom_tile_locations:
                self.custom_buttons[i][j].config(bg="red", state="disabled")
        else:
            print("Safe")
            self.reveal_tiles(i, j, self.custom_bombs, self.custom_buttons, self.custom_rows, self.custom_columns)

    # Function that calculates tile number counter and reveals valid tiles
    def reveal_tiles(self, i, j, bomb_type, button_type, rows, columns):
        # Boundaries so that recursion does not break the program
        if i < 0 or i >= rows or j < 0 or j >= columns:
            return
        if (i, j) in bomb_type:
            return
        if button_type[i][j]["state"] == "disabled" and button_type[i][j]["bg"] in ("light grey", "red"):
            return
        if button_type[i][j]["text"] == "🚩":
            return
        if button_type[i][j]["text"] == "💡":
            return
        
        # Reveals the tile
        button_type[i][j].config(bg="light grey", state="disabled")
        counter = 0
        neighboring_tiles = (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)
        for x, y in neighboring_tiles:
            if (x, y) in bomb_type:
                counter += 1
        if counter > 0:
            button_type[i][j].config(text=counter)
        else:
            for x, y in neighboring_tiles:
                # This is known as recursion, calling a function on itself and it repeats until one of the boundaries are triggered
                self.reveal_tiles(x, y, bomb_type, button_type, rows, columns)

    # Counts the number of revealed tiles, if it is equal to the total tiles minus the total bombs, the tile backgrounds turn green
    def win_condition(self, rows, columns, button_type, total_tile, total_bomb, timer_type):
        tile_counter = 0
        for i in range(rows):
            for j in range(columns):
                if button_type[i][j]["state"] == "disabled" and button_type[i][j]["bg"] == "light grey":
                    tile_counter += 1
        print(tile_counter)
        if tile_counter == total_tile - total_bomb:
            self.stop_timer(timer_type)
            for i in range(rows):
                for j in range(columns):
                    button_type[i][j].config(bg="light green", state="disabled")
                    if button_type[i][j]["text"] == "🚩":
                        button_type[i][j].config(state="disabled")

    # Running functions relevant to left-clicks
    def left_click(self, method, i ,j, rows, columns, button_type, total_tile, total_bomb, timer_type):
        method(i, j)
        self.win_condition(rows, columns, button_type, total_tile, total_bomb, timer_type)

    # Places flag if the tile text is empty and not disabed, and removing flags if the tile text is a flag and the tile is not disabled
    def right_click(self, i, j, button_type):
        if self.current_mode == "ghostsweeper":
            if button_type[i][j]["text"] == "" and not button_type[i][j]["state"] == "disabled":
                if len(self.ghostsweeper_bombs) == 0:
                    return
                if self.ghostsweeper_flag_counter == 0:
                    return
                else:
                    self.ghostsweeper_flag_counter -= 1
                    self.ghostsweeper_flag.config(text=f"💡: {self.ghostsweeper_flag_counter}")
                    button_type[i][j].config(text="💡")
            
            elif button_type[i][j]["text"] == "💡":
                self.ghostsweeper_flag_counter += 1
                self.ghostsweeper_flag.config(text=f"💡: {self.ghostsweeper_flag_counter}")
                button_type[i][j].config(text="")

            lit_tiles = []
            for i in range(GHOSTSWEEPER_GRID):
                for j in range(GHOSTSWEEPER_GRID):
                    if self.ghostsweeper_buttons[i][j]["bg"] == "light grey" or self.ghostsweeper_buttons[i][j]["text"] == "💡":
                        lit_tiles.append((i, j))

            extra_tiles = []
            for x, y in lit_tiles:
                surrounding = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
                for nx, ny in surrounding:
                    if 0 <= nx < GHOSTSWEEPER_GRID and 0 <= ny < GHOSTSWEEPER_GRID:
                        if (nx, ny) not in extra_tiles:
                            extra_tiles.append((nx, ny))
            lit_tiles.extend(extra_tiles)

            for i in range(GHOSTSWEEPER_GRID):
                for j in range(GHOSTSWEEPER_GRID):
                    if (i, j) not in lit_tiles:
                        self.ghostsweeper_buttons[i][j].config(bg="black", state="disabled")
                    else:
                        if self.ghostsweeper_buttons[i][j]["bg"] != "light grey":
                            self.ghostsweeper_buttons[i][j].config(bg="SystemButtonFace", state="normal")
                            
        if button_type[i][j]["text"] == "" and not button_type[i][j]["state"] == "disabled":
            if self.current_mode == "easy":
                self.easy_flag_counter -= 1
                self.easy_flag.config(text=f"🚩: {self.easy_flag_counter}")
                button_type[i][j].config(text="🚩")

            elif self.current_mode == "medium":
                self.medium_flag_counter -= 1
                self.medium_flag.config(text=f"🚩: {self.medium_flag_counter}")
                button_type[i][j].config(text="🚩")

            elif self.current_mode == "hard":
                self.hard_flag_counter -= 1
                self.hard_flag.config(text=f"🚩: {self.hard_flag_counter}")
                button_type[i][j].config(text="🚩")

            elif self.current_mode == "custom":
                self.custom_flag_counter -= 1
                self.custom_flag.config(text=f"🚩: {self.custom_flag_counter}")
                button_type[i][j].config(text="🚩")

        elif button_type[i][j]["text"] == "🚩" and not button_type[i][j]["state"] == "disabled":
            button_type[i][j].config(text="")
            if self.current_mode == "easy":
                self.easy_flag_counter += 1
                self.easy_flag.config(text=f"🚩: {self.easy_flag_counter}")

            elif self.current_mode == "medium":
                self.medium_flag_counter += 1
                self.medium_flag.config(text=f"🚩: {self.medium_flag_counter}")

            elif self.current_mode == "hard":
                self.hard_flag_counter += 1
                self.hard_flag.config(text=f"🚩: {self.hard_flag_counter}")
            
            elif self.current_mode == "custom":
                self.custom_flag_counter += 1
                self.custom_flag.config(text=f"🚩: {self.custom_flag_counter}")

    def reset(self, rows, columns, button_type, bomb_type, flag_type, total_bomb):
        bomb_type.clear()
        self.easy_flag_counter = EASY_TOTAL_BOMBS
        self.medium_flag_counter = MEDIUM_TOTAL_BOMBS
        self.hard_flag_counter = HARD_TOTAL_BOMBS
        self.ghostsweeper_flag_counter = 10

        try:
            self.custom_flag_counter = self.custom_total_bombs
        except AttributeError:
            pass

        if self.current_mode == "ghostsweeper":
            flag_type.config(text=f"💡: {self.ghostsweeper_flag_counter}")
        else:
            flag_type.config(text=f"🚩: {total_bomb}")

        for i in range(rows):
            for j in range(columns):
                button_type[i][j].config(bg="SystemButtonFace", state="normal", text="")

    def start_timer(self):
        self.easy_seconds_passed = 0
        self.medium_seconds_passed = 0
        self.hard_seconds_passed = 0
        self.custom_seconds_passed = 0
        self.ghostsweeper_seconds_left = 300
        self.update_timer()

    def update_timer(self):
        if self.current_mode == "easy":
            self.easy_timer.config(text=f"Timer: {self.easy_seconds_passed}")
            self.easy_seconds_passed += 1
            self.easy_timer_count = self.root.after(1000, self.update_timer)

        elif self.current_mode == "medium":
            self.medium_timer.config(text=f"Timer: {self.medium_seconds_passed}")
            self.medium_seconds_passed += 1
            self.medium_timer_count = self.root.after(1000, self.update_timer)

        elif self.current_mode == "hard":
            self.hard_timer.config(text=f"Timer: {self.hard_seconds_passed}")
            self.hard_seconds_passed += 1
            self.hard_timer_count = self.root.after(1000, self.update_timer)

        elif self.current_mode == "custom":
            self.custom_timer.config(text=f"Timer: {self.custom_seconds_passed}")
            self.custom_seconds_passed += 1
            self.custom_timer_count = self.root.after(1000, self.update_timer)

        elif self.current_mode == "ghostsweeper":
            self.ghostsweeper_timer.config(text=f"Timer: {self.ghostsweeper_seconds_left}")
            self.ghostsweeper_seconds_left -= 1
            self.ghostsweeper_timer_count = self.root.after(1000, self.update_timer)
            if self.ghostsweeper_seconds_left == -1:
                self.stop_timer(self.ghostsweeper_timer_count)
                for (i, j) in self.ghostsweeper_bombs:
                    self.ghostsweeper_buttons[i][j].config(text="👻")
                for (i, j) in self.ghostsweeper_tile_locations:
                    self.ghostsweeper_buttons[i][j].config(bg="red", state="disabled")


    def stop_timer(self, timer_type):
        if timer_type:
            self.root.after_cancel(timer_type)

if __name__ == "__main__":
    app = Minesweeper()
    app.run()