#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from typing import List


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 找到目标第一次出现和最后出现位置
class FindFirstAndLastPositionOfElementInSortedArray:

    # Runtime: 92 ms, faster than 49.41% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    # Memory Usage: 15.1 MB, less than 69.09% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    # 二分查找，分别找出最左边target位置 相等时right=mid-1，最右边target位置 相等时left=mid+1
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        rs = [-1, -1]
        self.nums = nums
        self.target = target

        if len(nums) == 0:
            return rs

        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        # 找出最左边
        def leftSearch(self, mid):
            self.right = mid - 1

        self.__binarySearch(leftSearch)
        if self.left >= len(nums) or nums[self.left] != target:
            return rs
        rs[0] = self.left

        # 找出最右边
        def rightSearch(self, mid):
            self.left = mid + 1

        self.__binarySearch(rightSearch)
        rs[1] = self.right
        return rs

    def __binarySearch(self, func):
        self.left = 0
        self.right = len(self.nums) - 1
        while self.left <= self.right:
            mid = self.left + (self.right - self.left) // 2
            midNum = self.nums[mid]
            if midNum == self.target:
                func(self, mid)
            if midNum > self.target:
                self.right = mid - 1
            if midNum < self.target:
                self.left = mid + 1

    # 线性扫描
    # Runtime: 96 ms, faster than 27.87% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    # Memory Usage: 15.2 MB, less than 45.01% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    # O(n)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rs = [-1, -1]
        for index, num in enumerate(nums):
            if num != target: continue
            if rs[0] == -1: rs[0], rs[-1] = index, index
            rs[1] = index
        return rs


if __name__ == "__main__":
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    nums = [1]
    target = 1
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6
    # nums = []
    # target = 0
    check = FindFirstAndLastPositionOfElementInSortedArray()
    rs = check.searchRange(nums, target)
    for num in rs:
        print(num)

    rs2 = check.searchRange2(nums, target)
    for num in rs2:
        print(num)
