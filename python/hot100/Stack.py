#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'


# Stack 先进后出，peek看栈顶元素
class Stack:

    def __init__(self):
        self.stack = []
        self.top = None

    def append(self, obj):
        self.top = obj
        self.stack.append(obj)

    def peek(self):
        return self.top

    def pop(self):
        item = self.stack.pop()
        length = len(self.stack)
        if length == 0:
            self.top = None
        else:
            self.top = self.stack[length - 1]
        return item

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return self.__len__() <= 0
