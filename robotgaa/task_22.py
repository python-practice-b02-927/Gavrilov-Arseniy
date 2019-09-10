#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    n=1
    i=1
    k=1
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
        n+=1
    while not( ( wall_is_on_the_left()) and ( wall_is_beneath())):
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        fill_cell()
        
        if wall_is_beneath():
            break
        move_down()
    
        
    if wall_is_on_the_left():
        for i in range (n-1):
            fill_cell()
            move_right()
        fill_cell()
        move_left(n-1)
            
        
        

        
    
    
    
        
    


if __name__ == '__main__':
    run_tasks()
