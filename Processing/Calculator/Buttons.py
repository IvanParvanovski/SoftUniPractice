from Config import BUTTON_WIDTH, \
                   BUTTON_HEIGHT, \
                   BUTTON_X_DIFF, \
                   BUTTON_Y_DIFF, \
                   BUTTONS_STARTING_X, \
                   BUTTONS_STARTING_Y, \
                   BUTTONS_COLOR

class NumberButtons:
    def __init__(self, number, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.number = number
        self.r, self.g, self.b = BUTTONS_COLOR
    
    def __create_button(self):          
        strokeWeight(5)  
        fill(self.r, self.g, self.b)
        rect(self.x, self.y, self.w, self.h, 30, 10, 20, 10)
    
    def __number_text(self):
        strokeWeight(5)  
        text_x = self.x - 10 + BUTTON_WIDTH / 2
        text_y = self.y + 10 + BUTTON_HEIGHT / 2
        fill(255)
        textSize(30)
        text(self.number, text_x, text_y)
    
    def solve(self):
        self.__create_button()
        self.__number_text()


def set_number_buttons():    
    """
    Get every number from 1-9, makes an object, and save it into a dict.
    The object includes (number as a digit, button_x, button_y, button_w, button_h)
    
    After the numbers are set they are called and shown.
    """
    
    def is_num_end_of_the_row(num):
        """
        When the num (counter) is at the end of the row (3 / 6 / 9) 
        it decreases button_y and starts new row.
        """
        
        return num % 3 == 0
    
    numbers_in_text = {
                1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine"
            }
    
    numbers_objects = dict()
    
    buttons_x, buttons_y = BUTTONS_STARTING_X, BUTTONS_STARTING_Y
    for num in range(1, 10):
        num_in_text = numbers_in_text[num]
        
        button_args = (num,
                       buttons_x, 
                       buttons_y,
                       BUTTON_WIDTH,
                       BUTTON_HEIGHT)
        
        num_button = NumberButtons(*button_args)
        numbers_objects[num_in_text] = num_button

        if is_num_end_of_the_row(num):
            buttons_x = BUTTONS_STARTING_X
            buttons_y -= 130
        else:
            buttons_x += 130
            
    
    for num_text in numbers_in_text.values():
        numbers_objects[num_text].solve()
        
