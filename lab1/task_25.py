#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
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
        
    move_down(2)
    i=1
    for i in range (4):
        krest()
        move_right(2)
    krest()
    move_left(2)
    move_up()

    




if __name__ == '__main__':
    run_tasks()
