#Painting area calculator
#September 29, 2021
#William Wu    

import math

def paint_calc(height, width, cover):
    paint_needed = math.ceil(height * width / cover)
    print(f"You will need {paint_needed} buckets of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)