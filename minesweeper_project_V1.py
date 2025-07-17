# Started on 16/07/25
# Version 1

import tkinter as tk
import random as r

# Constants
EASY_GRID = 9
MEDIUM_GRID = 16
EASY_TOTAL_TILES = 81
MEDIUM_TOTAL_TILES = 256
HARD_TOTAL_TILES = 480
EASY_TOTAL_BOMBS = 10
MEDIUM_TOTAL_BOMBS = 40
HARD_TOTAL_BOMBS = 100

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

        self.easy_button = tk.Button(frame, text="Easy", bg="green",
                                     font="Verdana 12 bold",
                                     command = lambda: self.show_frame("EasyFrame"))
        self.easy_button.grid(row = 1, column = 0, sticky = "NSEW")

        self.medium_button = tk.Button(frame, text="Medium", bg="yellow",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("MediumFrame"))
        self.medium_button.grid(row = 2, column = 0, sticky = "NSEW")

        self.hard_button = tk.Button(frame, text="Hard", bg="red",
                                     font="Verdana 12 bold",
                                     command = lambda: self.show_frame("HardFrame"))
        self.hard_button.grid(row = 3, column = 0, sticky = "NSEW")

        self.custom_button = tk.Button(frame, text="Custom", bg="pink",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("CustomFrame"))
        self.custom_button.grid(row = 4, column = 0, sticky = "NSEW")
        
        self.gamemodes_button = tk.Button(frame, text="Gamemodes", bg="orange",
                                     font = "Verdana 12 bold",
                                     command = lambda: self.show_frame("GamemodesFrame"))
        self.gamemodes_button.grid(row = 5, column = 0, sticky = "NSEW")

        self.leaderboard_button = tk.Button(frame, text="Leaderboard", bg ="cyan",
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

        return frame

    def create_medium_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

        return frame

    def create_hard_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")

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

if __name__ == "__main__":
    app = Minesweeper()
    app.run()