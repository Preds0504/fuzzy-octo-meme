"""
This the main module for the Minesweeper game
"""
from tkinter import Tk, Label, Frame
import settings
import utils
from cell import Cell

# variable equals a instantiantion of a window
root = Tk()

#Attributes for the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

#creates a frame and places it at the top starting at the left
top_frame = Frame(
    root,
    bg='black',
    width=1440,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

#Creates the Game title in the top frame
game_title = Label(
    top_frame,
    bg = 'black',
    fg = 'white',
    text = 'Minesweeper Game',
    font = ('', 48)
)

game_title.place(
    x=utils.width_prct(25),
    y=0
)

#creates a frame and places on the left below the top panel
left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

#creates a frame for the center where the game exists
center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

#The code below creates the grid of cells
#Needs nested loops to take in the proper size of the grid
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

#Will display the cell count label in the left frame
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)
#Calling this will randomize the cells in the game
Cell.randmize_mines()


#Run the window
root.mainloop()
