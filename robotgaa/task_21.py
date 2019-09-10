#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    i=1
    m=1
    k=0
    p=1
    move_right()
    move_down()
    for i in range (6):
        for m in range (12-k):
            fill_cell()
            move_right()
            move_down()
            fill_cell()
        k+=1
        m=1
        move_left()
        for p in range (12-k):
            fill_cell()
            move_up()
            move_left()
            fill_cell()
        k+=1
        p=1
        move_down()
    fill_cell()
    move_down()
        
        


if __name__ == '__main__':
    run_tasks()
