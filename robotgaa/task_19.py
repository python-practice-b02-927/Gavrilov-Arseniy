#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_above():
        move_up()
    while wall_is_beneath():
        move_right()
        if wall_is_on_the_right():
            break
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left() and not wall_is_beneath():
        move_left()
        
        
      
if __name__ == '__main__':
    run_tasks()  
