from tkinter import Button
import random
import settings
#Creates the Cells which the buttons will appear on
#This will be an object that will created many times
class Cell:
    #this is to be a list of cells
    all =[]
    #This is the default constructor 
    #by default the mines will be false
    #Will also initialize the button
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.y=y
        self.x=x

        #will add each cell to a list 
        Cell.all.append(self)
    # This creates the button that will be in each cell
    # location parameter will help us define its location in the window
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        #binds the buttons to run the clicking functions
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    #this is the function that runs after a click for left click
    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    #this is the function that runs after a click for right click
    def right_click_actions(self, event):
        print(event)
        print("I am right clicked")

    #this method will randomize the position of the mines
    @staticmethod
    def randmize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        

    #When the cells are added to the list
    #this function will allow it to show it as the coordinates
    #rather than the cell ids
    def __repr__(self):
        return f"Cell{self.x},{self.y}"