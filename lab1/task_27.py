#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    k=1
    n=0
    while True:
        for i in range(k):
            move_right()
            n+=1
            if wall_is_on_the_right():
                break
        if n==k:
            fill_cell()
            n=0
            k+=1
        if wall_is_on_the_right():
            break

if __name__ == '__main__':
    run_tasks()
