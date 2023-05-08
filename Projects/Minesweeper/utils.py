"""This module creates the ability to use percents to create the game frames"""

import settings

#function to create a new height from a percentage
#used to stop hard coded values and make the program more dynamic
def height_prct(percentage):
    """returns the height from using a percentage"""
    return (settings.HEIGHT / 100) * percentage

def width_prct(percentage):
    """returns the width from using a percentage"""
    return (settings.WIDTH / 100) * percentage
