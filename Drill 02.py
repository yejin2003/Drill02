from pico2d import *
import math
import os
open_canvas()

os.getcwd()
os.chdir('C:\\Users\\yejin2\\2024-2DGP\\Labs\\Lecture04_2D_Rendering')
# fill here

shape=0
x=400
y=90
i=0
grass=load_image('grass.png')
character=load_image('character.png')
while(1):
    clear_canvas_now()
    update_canvas()
    while(x<800):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=x+2
            y=90
    while(y<600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y=y+2
            x=799
    while(x>0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=x-2
            y=600
    while(y>0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y=y-2
            x=30
            shape=1
    

close_canvas()

