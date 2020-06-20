#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from typing import List
import sys


class SearchInRotatedSortedArray:

    # Runtime: 28 ms, faster than 75.34% of Python online submissions for Search in Rotated Sorted Array.
    # Memory Usage: 13.1 MB, less than 35.14% of Python online submissions for Search in Rotated Sorted Array.
    # 算法基于一个事实，数组从任意位置劈开后，至少有一半是升序的
    def search3(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            midNum = nums[mid]
            if midNum == target:
                return mid
            if nums[left] <= midNum:
                # 左边升序
                if midNum > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右边升序
                if midNum < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    # Runtime: 24 ms, faster than 92.71% of Python online submissions for Search in Rotated Sorted Array.
    # Memory Usage: 13 MB, less than 64.31% of Python online submissions for Search in Rotated Sorted Array.
    # 将数组分成两段有序
    # 把 nums [ mid ] 和 target 同时与 nums [ 0 ] 比较，如果它俩都大于 nums [ 0 ] 或者都小于 nums [ 0 ]，那么就代表它俩在同一段。
    def search2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            midNum = nums[mid]
            if (nums[0] <= target) == (nums[0] <= midNum):
                midNum = nums[mid]
            else:
                if target < nums[0]:
                    midNum = -sys.maxsize - 1
                else:
                    midNum = sys.maxsize
            if midNum < target:
                left = mid + 1
            elif midNum > target:
                right = mid - 1
            else:
                return mid
        return -1

    # Runtime: 36 ms, faster than 90.09% of Python3 online submissions for Search in Rotated Sorted Array.
    # Memory Usage: 14.2 MB, less than 6.29% of Python3 online submissions for Search in Rotated Sorted Array.
    # 规律可得出（位置 + 偏移 ）% 数组的长度 = 原来的位置
    # 可根据原有位置就可以进行二分查找了
    # 二分
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length < 3:
            for index, num in enumerate(nums):
                if num == target:
                    return index
            return -1

        left = 0
        right = length - 1
        # 找最大值，求偏移量
        while left < right:
            mid = left + (right - left) // 2
            mid_num = nums[mid]
            # 中间的小于右边尾巴的，最小值一定右边
            if mid_num > nums[right]:
                left = mid + 1
            else:
                right = mid
        bias = left
        # 对偏移前的位置进行二分查找，通过偏移量求出对应值
        left = 0
        right = length - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pos = (mid + bias) % length
            mid_value = nums[mid_pos]
            if mid_value == target: return mid_pos
            if mid_value > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == "__main__":
    # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    # Output: 4
    #
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0
    # check = SearchInRotatedSortedArray()
    # print(check.search2(nums, target))

    # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    # Output: -1
    #
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 3
    # check = SearchInRotatedSortedArray()
    # print(check.search(nums, target))

    nums = [1, 3]
    target = 3
    check = SearchInRotatedSortedArray()
    print(check.search2(nums, target))
    print(check.search3(nums, target))

    # nums = [1, 3, 5]
    # target = 5
    # check = SearchInRotatedSortedArray()
    # print(check.search(nums, target))
    # print(check.search2(nums, target))
