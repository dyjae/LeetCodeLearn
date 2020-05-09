#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from typing import List


class FirstMissingPositive:

    # Runtime: 36 ms, faster than 55.98% of Python3 online submissions for First Missing Positive.
    # Memory Usage: 13.9 MB, less than 8.70% of Python3 online submissions for First Missing Positive.
    # 运用的一位对应一个数的思路
    # 将存在的数都置成负数，正数的位置就是最小不存在
    # TODO https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode/
    def firstMissingPositive1(self, nums: List[int]) -> int:
        # 直接定位1有没有
        if 1 not in nums:
            return 1

        # 将小于1  和  大于长度的数 置为1，确保没有负数和超过len(nums)的数
        for i, num in enumerate(nums):
            if num < 1 or num > len(nums):
                nums[i] = 1

        # i~len(nums) 对应存在数字的下标置为负数, 因为len=n将n放到0的位置
        for i, num in enumerate(nums):
            num = abs(num)
            if num == len(nums):
                nums[0] = -abs(nums[0])
            elif num:
                nums[num] = -abs(nums[num])

        # 第一个下标不为负数   的就是上面循环没有循环到的数
        for i, num in enumerate(nums):
            if i and nums[i] > 0:
                return i

        # 0的位置对应的是n
        if nums[0] > 0:
            return len(nums)

        # 都存在，则最小的为 len+1
        return len(nums) + 1

    # 排序，遍历
    # Runtime: 32 ms, faster than 81.80% of Python3 online submissions for First Missing Positive.
    # Memory Usage: 13.9 MB, less than 8.70% of Python3 online submissions for First Missing Positive.
    def firstMissingPositive(self, nums: List[int]) -> int:
        sNums = sorted(nums)
        minN = 0
        for num in sNums:
            if num < 0 or num == minN: continue
            if num != minN + 1: return minN + 1
            minN = num
        return minN + 1


if __name__ == "__main__":
    nums = [1, 2, 0]  # 3
    nums2 = [3, 4, -1, 1]  # 2
    nums3 = [7, 8, 9, 11, 12]  # 1
    check = FirstMissingPositive()
    print(check.firstMissingPositive(nums))
    print(check.firstMissingPositive(nums2))
    print(check.firstMissingPositive(nums3))
