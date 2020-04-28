#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

# https://leetcode.com/problems/lru-cache/

from collections import OrderedDict


# Runtime: 204 ms, faster than 63.57% of Python3 online submissions for LRU Cache.
# Memory Usage: 23 MB, less than 6.06% of Python3 online submissions for LRU Cache.
class LRUCache:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        # 尾部添加,
        self.__dict = OrderedDict()

    def get(self, key: int) -> int:
        v = self.__dict.get(key, -1)
        if v != -1: self.__change_pos(key, v)
        return v

    def put(self, key: int, value: int) -> None:
        self.__change_pos(key, value)
        # 头部删除
        if len(self.__dict) > self.__capacity: self.__dict.popitem(last=False)

    def __change_pos(self, key, value):
        if self.__dict.keys().__contains__(key):
            self.__dict.__delitem__(key)
        self.__dict[key] = value


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    print(cache.put(3, 3))
    print(cache.get(2))
    print(cache.put(4, 4))
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
