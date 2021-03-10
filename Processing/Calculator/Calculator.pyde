from Config import WINDOW_SIZE, \
                   WINDOW_WIDTH,\
                   WINDOW_LENGTH, \
                   BACKGROUND_COLOR
                   
                   
from Buttons import set_number_buttons

    
def setup():
    background(*BACKGROUND_COLOR)
    size(*WINDOW_SIZE)
    
    
def draw():
    set_number_buttons()
    
