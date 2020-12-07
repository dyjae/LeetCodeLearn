#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 56.MergeIntervals.py
# DATE : 2020/11/13 09:18

__author__ = 'Jae'

from typing import List


# https://leetcode.com/problems/merge-intervals/
class MergeIntervals:

    def __init__(self):
        self.rs = []

    # 方法2的简便写法
    def merge3(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else:
                out.append(i)
        return out

    # Runtime: 228 ms, faster than 5.67% of Python3 online submissions for Merge Intervals.
    # Memory Usage: 16.1 MB, less than 12.85% of Python3 online submissions for Merge Intervals.
    # 先进行排序再进行解法一
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        def take_first(elem):
            return elem[1]

        intervals.sort(key=take_first)
        for item in intervals:
            self.__checkMerge2(item)
        return self.rs

    def __checkMerge2(self, checkList: List[int]):
        removes = []
        minV = checkList[0]
        maxV = checkList[-1]
        for item in reversed(self.rs):
            itemMin = item[0]
            itemMax = item[-1]
            # 有交集
            if self.__checkIntersection(minV, maxV, itemMin, itemMax):
                # 记录移除
                removes.append(item)
                # 改变区间
                minV = min(minV, itemMin)
                maxV = max(maxV, itemMax)
            else:
                break
        for item in removes:
            self.rs.remove(item)
        self.rs.append([minV, maxV])

    # 分解求解
    # Runtime: 104 ms, faster than 6.59% of Python3 online submissions for Merge Intervals.
    # Memory Usage: 16 MB, less than 23.60% of Python3 online submissions for Merge Intervals.
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        for item in intervals:
            self.__checkMerge(item)
        return self.rs

    def __checkMerge(self, checkList: List[int]):
        removes = []
        minV = checkList[0]
        maxV = checkList[-1]
        for item in reversed(self.rs):
            itemMin = item[0]
            itemMax = item[-1]
            # 有交集
            if self.__checkIntersection(minV, maxV, itemMin, itemMax):
                # 记录移除
                removes.append(item)
                # 改变区间
                minV = min(minV, itemMin)
                maxV = max(maxV, itemMax)
        for item in removes:
            self.rs.remove(item)
        self.rs.append([minV, maxV])

    # 检查交集
    def __checkIntersection(self, minA, maxA, minB, maxB) -> bool:
        if minA <= minB <= maxA: return True
        if minA <= maxB <= maxA: return True
        if minB <= minA <= maxA <= maxB: return True
        return False


if __name__ == "__main__":
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [4, 5]]
    # intervals = [[1, 4], [0, 4]]
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    check = MergeIntervals()
    print(check.merge3(intervals))
