# Started on 16/07/25
# Version 1

import tkinter as tk
import random as r

# Constants
EASY_GRID = 9
MEDIUM_GRID = 16
HARD_GRID = 20
EASY_TOTAL_TILES = 81
MEDIUM_TOTAL_TILES = 256
HARD_TOTAL_TILES = 400
EASY_TOTAL_BOMBS = 10
MEDIUM_TOTAL_BOMBS = 40
HARD_TOTAL_BOMBS = 80

class Minesweeper:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper Game")

        self.container = tk.Frame(self.root)
        self.container.grid(row = 0, column = 0, sticky = "NESW")
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)      
        

        self.frames = {}
        self.frames["PlayFrame"] = self.create_play_frame()
        self.frames["TutorialFrame"] = self.create_tutorial_frame()
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["EasyFrame"] = self.create_easy_frame()
        self.frames["MediumFrame"] = self.create_medium_frame()
        self.frames["HardFrame"] = self.create_hard_frame()
        self.frames["CustomFrame"] = self.create_custom_frame()
        self.frames["GamemodesFrame"] = self.create_gamemodes_frame()
        self.frames["LeaderboardFrame"] = self.create_leaderboard_frame()

        self.show_frame("PlayFrame")
            
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)      
        
    def run(self):
        self.root.mainloop()

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

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
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        title_label = tk.Label(frame, text="Tutorial", font="Verdana 22 bold")
        title_label.grid(row = 0, column = 0, columnspan = 2)

        return frame

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
                                     command = lambda: self.show_frame("CustomFrame"))
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
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        self.easy_buttons = []
        self.easy_bombs = []

        for i in range(EASY_GRID):
            easy_row = []
            for j in range(EASY_GRID):
                easy_tile = tk.Button(frame, borderwidth=1, width = 2, height = 1)
                easy_tile.grid(row = i, column = j, sticky = "NSEW")
                easy_tile.bind('<Button-1>', lambda event, x=i, y=j: self.left_click(self.easy_clicks, x, y, EASY_GRID, self.easy_buttons, EASY_TOTAL_TILES, EASY_TOTAL_BOMBS))
                easy_tile.bind('<Button-3>', lambda event, x=i, y=j: self.right_click(x, y, self.easy_buttons))
                easy_row.append(easy_tile)
            self.easy_buttons.append(easy_row)

        for i in range(EASY_GRID):
            frame.grid_rowconfigure(i, weight = 1)
        for j in range(EASY_GRID):
            frame.grid_columnconfigure(j, weight = 1)

        return frame

    def create_medium_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        self.medium_buttons = []
        self.medium_bombs = []

        for i in range(MEDIUM_GRID):
            medium_row = []
            for j in range(MEDIUM_GRID):
                medium_tile = tk.Button(frame, borderwidth=1, width = 2, height = 1)
                medium_tile.grid(row = i, column = j, sticky = "NSEW")
                medium_tile.bind('<Button-1>', lambda event, x=i, y=j: self.left_click(self.medium_clicks, x, y, MEDIUM_GRID, self.medium_buttons, MEDIUM_TOTAL_TILES, MEDIUM_TOTAL_BOMBS))
                medium_tile.bind('<Button-3>', lambda event, x=i, y=j: self.right_click(x, y, self.medium_buttons))
                medium_row.append(medium_tile)
            self.medium_buttons.append(medium_row)

        for i in range(MEDIUM_GRID):
            frame.grid_rowconfigure(i, weight = 1)
        for j in range(MEDIUM_GRID):
            frame.grid_columnconfigure(j, weight = 1)

        return frame

    def create_hard_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        self.hard_buttons = []
        self.hard_bombs = []

        for i in range(HARD_GRID):
            hard_row = []
            for j in range(HARD_GRID):
                hard_tile = tk.Button(frame, borderwidth=1, width = 2, height = 1)
                hard_tile.grid(row = i, column = j, sticky = "NSEW")
                hard_tile.bind('<Button-1>', lambda event, x=i, y=j: self.left_click(self.hard_clicks, x, y, HARD_GRID, self.hard_buttons, HARD_TOTAL_TILES, HARD_TOTAL_BOMBS))
                hard_tile.bind('<Button-3>', lambda event, x=i, y=j: self.right_click(x, y, self.hard_buttons))
                hard_row.append(hard_tile)
            self.hard_buttons.append(hard_row)

        for i in range(HARD_GRID):
            frame.grid_rowconfigure(i, weight = 1)
        for j in range(HARD_GRID):
            frame.grid_columnconfigure(j, weight = 1)

        return frame

    def create_custom_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        return frame
    
    def create_gamemodes_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        return frame

    def create_leaderboard_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        return frame

    def easy_clicks(self, i, j):
        # If the tile if flagged, user cannot reveal it until it is unflagged
        if self.easy_buttons[i][j]["text"] == "🚩":
            return
        # It will be the first click if the bombs list is empty
        if len(self.easy_bombs) == 0:
            self.easy_tile_locations = [(i, j) for i  in range(EASY_GRID) for j in range(EASY_GRID)]
            self.surrounding_tiles = (i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)
            easy_excluded_tiles = []
            for x, y in self.surrounding_tiles:
                if 0 <= x < EASY_GRID and 0 <= y < EASY_GRID:
                    easy_excluded_tiles.append((x, y))
            easy_safe_tiles = []
            for tile in self.easy_tile_locations:
                if tile not in easy_excluded_tiles:
                    easy_safe_tiles.append(tile)
            self.easy_bombs = r.sample(easy_safe_tiles, k=EASY_TOTAL_BOMBS)

        print(f"You clicked: ({i}, {j})") # For Debugging
        if (i, j) in self.easy_bombs:
            print("Bomb")
            for (i, j) in self.easy_bombs:
                self.easy_buttons[i][j].config(text="💣")
            for (i, j) in self.easy_tile_locations:
                self.easy_buttons[i][j].config(bg="red", state="disabled")
        else:
            print("Safe")
            self.reveal_tiles(i, j, self.easy_bombs, self.easy_buttons, EASY_GRID)

    def medium_clicks(self, i, j):
        if self.medium_buttons[i][j]["text"] == "🚩":
            return
        if len(self.medium_bombs) == 0:
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
        if (i, j) in self.medium_bombs:
            print("Bomb")
            for (i, j) in self.medium_bombs:
                self.medium_buttons[i][j].config(text="💣")
            for (i, j) in self.medium_tile_locations:
                self.medium_buttons[i][j].config(bg="red", state="disabled")
        else:
            print("Safe")
            self.reveal_tiles(i, j, self.medium_bombs, self.medium_buttons, MEDIUM_GRID)

    def hard_clicks(self, i, j):
        if self.hard_buttons[i][j]["text"] == "🚩":
            return
        if len(self.hard_bombs) == 0:
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
        if (i, j) in self.hard_bombs:
            print("Bomb")
            for (i, j) in self.hard_bombs:
                self.hard_buttons[i][j].config(text="💣")
            for (i, j) in self.hard_tile_locations:
                self.hard_buttons[i][j].config(bg="red", state="disabled")
        else:
            print("Safe")
            self.reveal_tiles(i, j, self.hard_bombs, self.hard_buttons, HARD_GRID)

    def reveal_tiles(self, i, j, bomb_type, button_type, grid_size):
        # Boundaries
        if i < 0 or i >= grid_size or j < 0 or j >= grid_size:
            return
        if (i, j) in bomb_type:
            return
        if button_type[i][j]["state"] == "disabled":
            return

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
                self.reveal_tiles(x, y, bomb_type, button_type, grid_size)

    def win_condition(self, grid_size, button_type, total_tile, total_bomb):
        tile_counter = 0
        for i in range(grid_size):
            for j in range(grid_size):
                if button_type[i][j]["state"] == "disabled":
                    tile_counter += 1
        print(tile_counter)
        if tile_counter == total_tile - total_bomb:
            for i in range(grid_size):
                for j in range(grid_size):
                    button_type[i][j].config(bg="light green", state="disabled")

    def left_click(self, method, i ,j, grid_size, button_type, total_tile, total_bomb):
        method(i, j)
        self.win_condition(grid_size, button_type, total_tile, total_bomb)

    def right_click(self, i, j, button_type):
        if button_type[i][j]["text"] == "":
            button_type[i][j].config(text="🚩")
        elif button_type[i][j]["text"] == "🚩":
            button_type[i][j].config(text="")

if __name__ == "__main__":
    app = Minesweeper()
    app.run()