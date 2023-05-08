"""This module is for the cell class and most of the game logic"""
from tkinter import Button, Label
import random
import ctypes
import sys
import settings

#Creates the Cells which the buttons will appear on
#This will be an object that will created many times
class Cell:
    """
    Creates the Cells which the buttons will appear on
    This will be an object that will created many times to create a grid
    """
    #this is to be a list of cells
    all =[]
    #this value will be changed to help display cells left
    cell_count = settings.CELL_COUNT
    #using this to make the label count accessible for the whole class
    cell_count_label_object = None
    def __init__(self, x_coord, y_coord, is_mine=False):
        """
        This is the default constructor
        by default the mines will be false
        Will also initialize the button
        """
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_opened = False
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.is_mine_candidate = False
        #will add each cell to this list
        Cell.all.append(self)

    def create_btn_object(self, location):
        """
        This creates the button that will be in each cell
        location parameter will help us define its location in the window
        """
        btn = Button(
            location,
            width=12,
            height=4,
        )
        #binds the buttons to run the clicking functions
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        """Creates a label to show cells left"""
        lbl = Label(
            location,
            bg='black',
            fg = 'white',
            text=f"Cells Left:{Cell.cell_count}",
            width = 12,
            height = 4,
            font = ("Ariel", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        """
        this is the function that runs after a left click
        """
        if self.is_mine:
            self.show_mine()
        else:
            #this shows all cells that surround a cell with 0 mines to speed the game up
            if self.surrounded_cells_mines_length == 0:
                #cell_obj is the place holder for each element in the loop
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            #if the mines count is equal to the cells left count, player wins
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations, You won the Game!',
                "Game Over", 0)
            #will cancel left and right clicking for opened cells
            self.cell_btn_object.unbind('<Button-1>')
            self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self,x_coord,y_coord):
        """
        needs to return a cell object, given x and y
        """
        for cell in Cell.all:
            if cell.x_coord == x_coord and cell.y_coord == y_coord:
                return cell
        return None

    @property
    def surrounded_cells(self):
        """Determines the cells around the clicked cell"""
        cells = [
            self.get_cell_by_axis(self.x_coord-1, self.y_coord-1),
            self.get_cell_by_axis(self.x_coord-1, self.y_coord),
            self.get_cell_by_axis(self.x_coord-1, self.y_coord+1),
            self.get_cell_by_axis(self.x_coord, self.y_coord-1),
            self.get_cell_by_axis(self.x_coord+1, self.y_coord-1),
            self.get_cell_by_axis(self.x_coord+1, self.y_coord),
            self.get_cell_by_axis(self.x_coord+1, self.y_coord+1),
            self.get_cell_by_axis(self.x_coord, self.y_coord+1)
        ]
        #for loop in one line to filter out the nones in the list
        #called list comprehension
        surrounded_cells = [cell for cell in cells if cell is not None]
        return surrounded_cells

    @property
    def surrounded_cells_mines_length(self):
        """counts how many mines are around the cell"""
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        """
        This method shows cells around a non-mine cell
        """
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length)
            #the if structure each time a cell is clicked
            # it will replace the old label with the updated one
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f"Cells Left:{Cell.cell_count}"
                )
            #This to reset the color of a minecandidate after being left-clicked
            self.cell_btn_object.configure(
                bg = 'SystemButtonFace'
            )
        #This will mark if the cell has been opened
        self.is_opened = True


    def show_mine(self):
        """Will run when a mine must be displayed from being clicked"""
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'you clicked on a mine', 'Game Over', 0)
        sys.exit()


    def right_click_actions(self, event):
        """
        This will be run once a cell has been right-clicked
        """
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg = 'orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randmize_mines():
        """
        Method will randomize the mines on the grid
        """
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


    def __repr__(self):
        """
        When the cells are added to the list
        this function will allow it to show it as the coordinates
        rather than the cell ids
        """
        return f"Cell{self.x_coord},{self.y_coord}"
