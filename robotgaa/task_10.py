#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    while not wall_is_not_the_right():
        if wall_is_beneath():
            fill_cell()
        if wall_is_above
            fill_cell()
        move_right()
    


if __name__ == '__main__':
    run_tasks()
