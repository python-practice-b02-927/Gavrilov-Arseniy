#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def krest():
        fill_cell()
        move_right()
        move_down()
        fill_cell()
        move_up()
        move_up()
        fill_cell()
        move_down()
        fill_cell()
        move_right()
        fill_cell()
        
    def krest2():
        fill_cell()
        move_left()
        move_down()
        fill_cell()
        move_up()
        move_up()
        fill_cell()
        move_down()
        fill_cell()
        move_left()
        fill_cell()
        
    move_down(1)
    i=1
    k=1
    p=1
    z=1
    for k in range (2):
        for i in range (9):
            krest()
            move_right(2)
        krest()
        move_down(4)
        for p in range(9):
            krest2()
            move_left(2)
        krest2()
        move_down(4)
    for z in range (9):
            krest()
            move_right(2)
    krest()
    move_left(38)
    move_up()    


if __name__ == '__main__':
    run_tasks()
