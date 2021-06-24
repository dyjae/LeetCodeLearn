#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 31.NextPermutation
# DATE : 2021/06/24 08:19

__author__ = 'Jae'

# https://leetcode.com/problems/next-permutation/
from typing import List


class NextPermutation:

    def nextPermutation1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i < 0:
            nums.sort()
            return

        j = n - 1
        while j >= 0:
            if nums[j] > nums[i]:
                break
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]

    # Runtime: 44 ms, faster than 53.52% of Python3 online submissions for Next Permutation.
    # Memory Usage: 14 MB, less than 92.40% of Python3 online submissions for Next Permutation.
    def nextPermutation(self, nums: List[int]) -> None:
        print(nums)
        changeIndex = -1
        for index in range(len(nums) - 1, 0, -1):
            if nums[index] > nums[index - 1]:
                changeIndex = index - 1
                break
        if changeIndex == -1:
            nums = nums.reverse()
            return
        for index in range(len(nums) - 1, changeIndex, -1):
            if nums[index] > nums[changeIndex]:
                nums[index], nums[changeIndex] = nums[changeIndex], nums[index]
                break
        if changeIndex < len(nums) - 2:
            i = changeIndex + 1
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        print(nums)


if __name__ == "__main__":
    check = NextPermutation()
    nums = [1, 2, 3]
    nums1 = [1, 3, 2]

    check.nextPermutation(nums)
    check.nextPermutation(nums1)
