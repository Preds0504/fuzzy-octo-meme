#Library used to import classes to help create a window
from tkinter import *
import settings
import utils

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
    bg='red',
    width=1440,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

#creates a frame and places on the left below the top panel
left_frame = Frame(
    root,
    bg='blue',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=180)

#Run the window
root.mainloop()