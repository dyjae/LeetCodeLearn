#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def log(self):
        print(self.val)
        if self.next is not None:
            self.next.log()
