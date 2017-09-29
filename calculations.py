# Created by: Scarlett Gao
# Created on: Aug 2016
# Created for: ICS3U
# This program does basic math

import ui

def equation1_touch_up_inside(sender):
    # displays the answer to equation 1
    
    #view['answer1_label'].text = str(5+2^3)
    # in python "^" is a bitwise operator and not for exponents
    # should have used "str(5+2**3)"
    view['answer1_label'].text = str(5+2**3)
    
def equation2_touch_up_inside(sender):
    # displays the answer to equation 2
    view['answer2_label'].text = str(4/2+5)
    
def equation3_touch_up_inside(sender):
    # displays the answer to equation 3
    view['answer3_label'].text = str(3+4*2)
    
def equation4_touch_up_inside(sender):
    # displays the answer to equation 4
    view['answer4_label'].text = str(7-3+2)

view = ui.load_view()
view.present('full_screen')
