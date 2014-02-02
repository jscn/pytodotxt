#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class PriorityExtractor(object):

    def __init__(self, task):
        self.task = task

    def extract_priority(self):
        if len(self.task) > 4 and self.task[0] == '(' and self.task[2] == ')' and self.task[3] == ' ':
            return self.task[1]

    def __str__(self):
        return self.extract_priority()


class Task(object):

    def __init__(self, task):
        self.task = task
        self.priority = PriorityExtractor(task)
        self.text = self.get_text()

    def get_text(self):
        return self.task


class TaskList(object):

    def __init__(self, filename):
        self.filename = filename

    def __len__(self):
        return 8

    def __getitem__(self, key):
        return Task('')
