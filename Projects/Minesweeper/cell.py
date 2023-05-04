from tkinter import Button
#Creates the Cells which the buttons will appear on
#This will be an object that will created many times
class Cell:
    #This is the default constructor 
    #by default the mines will be false
    #Will also initialize the button
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
    # This creates the button that will be in each cell
    # location parameter will help us define its location in the window
    def create_btn_object(self, location):
        btn = Button(
            location,
            text='Text'
        )
        self.cell.btn_object = btn