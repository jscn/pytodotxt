#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from pytodotxt import Task, TaskList

def test_contains_the_correct_number_of_items():
    tasks = TaskList('todo.txt')
    assert len(tasks) == 8

def test_supports_indexing():
    tasks = TaskList('todo.txt')
    assert tasks[0] is not None

def test_get_item_returns_a_task_object():
    tasks = TaskList('todo.txt')
    assert type(tasks[0]) == Task

def test_task_sets_priority():
    task = Task('(A) Call Mom @Phone +Family')
    assert '{0}'.format(task.priority) == 'A'

    task = Task('(B) Call Mom @Phone +Family')
    assert '{0}'.format(task.priority) == 'B'

def test_task_sets_text_when_only_text_is_included():
    task  = Task('Call Mom')
    assert task.text == 'Call Mom'

def test_task_sets_text_when_priority_is_set():
    task = Task('(B) Call Mom @Phone +Family')
    assert task.text == 'Call Mom'

def test_task_sets_text_when_priority_is_not_set():
    task = Task('Call Mom @Phone +Family')
    assert task.text == 'Call Mom'
    
