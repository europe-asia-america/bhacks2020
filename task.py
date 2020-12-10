#!/usr/bin/env python3

import random
import sys
import datetime
import numpy as np
import tasklib
from tasklib import TaskWarrior
import tzlocal
import hyperparameters
import os

RC = os.environ.get('TASKRC') or "~/.taskrc"
if not os.path.exists(RC):
    import subprocess
    subprocess.run(["touch", RC])
TASK_DATA = os.environ.get('TASK_DATA') or "~/.taskdb"
if not os.path.exists(TASK_DATA):
    subprocess.run(["mkdir", TASK_DATA])
tw = TaskWarrior(taskrc_location=RC, data_location=TASK_DATA)

# create a datetime object with tomorrow's date but time as of this moment
tom = datetime.datetime.today() + datetime.timedelta(days=1)
# correct time to midnight
tom = tom.replace(hour=0, minute=0, second=0)
# make datetime object "aware"
tom = tom.replace(tzinfo=tzlocal.get_localzone())


def priority_sort(task_list):
    """
    Return task list sorted by priority, descending order
    """
    return sorted(task_list, key=lambda t: -t['priority'])


def softmax(av, tau=hyperparameters.tau):
    """
    av = action value vector
    tau = temperature

    returns an array that is a weighted probability distribution
    """
    # convert list into np.array
    av = np.array(av)
    # np.exp is applied element-wise
    softm = np.exp(av / tau) / np.sum(np.exp(av / tau))
    return softm


def softmax_selection(tasks):
    """
    Choose a task from list of tasks based on softmax probability distribution
    """
    sm_dist = softmax([float(task["priority"]) + hyperparameters.softmax_urgency_discount_rate
        * float(task["urgency"]) for task in tasks], tau=1)
    return np.random.choice(tasks, p=sm_dist)


def get_next_task():
    """
    Return the next task to be done
    AKA the next reading material to be read
    """
    if hyperparameters.action_selection_method == "softmax":
        list_of_current_tasks = tw.tasks.pending()
        # remove daily recurring tasks that aren't due by 0000 hours the next day
        list_of_current_tasks = [task for task in list_of_current_tasks if not(((task["recur"] in ["P1D", "daily", "P2D"]) and task["due"] > tom) or task["depends"])]
        if len(list_of_current_tasks) > 0:
            current = softmax_selection(list_of_current_tasks)
            return current
        else:
            return None

def add_new_task(description, project=None, due=None):
    if project != '' and due != '':
        new_task = tasklib.Task(tw, description=description, project=project, due=due)
    elif due != '':
        new_task = tasklib.Task(tw, description=description, due=due)
    elif project != '':
        new_task = tasklib.Task(tw, description=description, project=project)
    else:
        new_task = tasklib.Task(tw, description=description)
    new_task.save()


def delete_task(task_id):
    task = tw.tasks.filter(id=task_id)[0]
    task.delete()
    task.save()


def mark_task_as_done(task_id):
    task = tw.tasks.filter(id=task_id)[0]
    task.done()
    task.save()


def progress_task(task_id):
    # slightly increase priority
    task = tw.tasks.filter(id=task_id)[0]
    task['priority'] = float(task['priority']) * 1.2
    task.save()


def skip_task(task_id):
    # slightly reduce priority
    task = tw.tasks.filter(id=task_id)[0]
    task['priority'] = float(task['priority']) * 0.8
    task.save()

feedback = {
        "delete": delete_task,
        "done": mark_task_as_done,
        "progress": progress_task,
        "skip": skip_task
        }
