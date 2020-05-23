#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def log(self):
        print(self.value)
        if self.next is not None:
            self.next.log()
