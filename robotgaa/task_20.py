#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    i=1
    for i in range (6):
        k=1
        l=1
        for k in range(27):
            move_right()
            fill_cell()
        move_down()
        for l in range(27)
            move_left()
            fill_cell()
        move_down()


if __name__ == '__main__':
    run_tasks()
