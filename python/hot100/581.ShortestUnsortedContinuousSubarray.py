#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

import sys
from typing import List


class ShortestUnsortedContinuousSubarray:

    def findUnsortedSubarray4(self, nums: List[int]) -> int:
        # 只有一个数时
        if len(nums) == 1:
            return 0

        # 找出最大窗口
        left, right = 0, len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                left = i - 1
                break
            left = i
        print("left:", left, " right:", right)

        if left >= right:  # sorted
            return 0

        for j in range(len(nums) - 2, -1, -1):
            if nums[j] > nums[j + 1]:
                right = j + 1
                break
            right = j
        print("left:", left, " right:", right)

        # if left > right:
        #     print(">>", left, right)
        #     return left - right + 1

        minVal = min(nums[left:right + 1])
        maxVal = max(nums[left:right + 1])

        # 找出左边最小值
        print("min, max:", minVal, maxVal)
        while left >= 0:
            if nums[left] > minVal:
                left -= 1
            else:
                break
        # 找出右边最大值
        while right <= len(nums) - 1:
            if nums[right] < maxVal:
                right += 1
            else:
                break

        print("l, r:", left, right)
        return right - left - 1

        # ===============================================

    # 和方法一一样
    def findUnsortedSubarray3(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sort = sorted(nums)
        i, j = 0, len(nums) - 1
        left, right = 0, len(nums) - 1

        # Find left change
        while i < len(nums) and nums[i] == sort[i]:
            i += 1

        # Find right change
        while j >= i and nums[j] == sort[j]:
            j -= 1

        print(i, j)
        return j - i + 1

        # ===============================================

    # 同方法一
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sort = sorted(nums)
        left, right = 0, len(nums) - 1

        # Find left change
        for i in range(len(nums)):
            if nums[i] != sort[i]:
                left = i
                break

        # Find right change
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != sort[i]:
                right = i
                break

        # Judge the case is sorted or not
        ans = right - left + 1
        # 判断已经排序
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return ans
        return 0

    # Runtime: 208 ms, faster than 84.71% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
    # Memory Usage: 15.1 MB, less than 5.00% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        sortedNum = sorted(nums)
        start, end = -1, -1
        for i in range(len(nums)):
            if nums[i] != sortedNum[i]:
                start = i
                break
        if start == -1: return 0  # 已经排序过
        for i in range(len(nums) - 1, start, -1):
            if nums[i] != sortedNum[i]:
                end = i
                break
        return end - start + 1


if __name__ == "__main__":
    list = [2, 6, 4, 8, 10, 9, 15]  # 5
    # list = [1, 2, 3, 4] #0
    # list = [2, 1]  # 2

    check = ShortestUnsortedContinuousSubarray()
    print(check.findUnsortedSubarray1(list))
