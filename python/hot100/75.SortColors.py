#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 75.SortColors.py
# DATE : 2020/12/15 09:42

__author__ = 'Jae'

# https://leetcode.com/problems/sort-colors/
from typing import List


class SortColors:

    # https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
    # 移动one_pos指针,同解法3
    def sortColors5(self, nums):
        zero_pos, one_pos, two_pos = 0, 0, len(nums) - 1

        while one_pos <= two_pos:
            if nums[one_pos] == 0:
                nums[zero_pos], nums[one_pos] = nums[one_pos], nums[zero_pos]
                one_pos += 1
                zero_pos += 1
            elif nums[one_pos] == 1:
                one_pos += 1
            else:
                nums[one_pos], nums[two_pos] = nums[two_pos], nums[one_pos]
                two_pos -= 1

    # Runtime: 32 ms, faster than 68.25% of Python3 online submissions for Sort Colors.
    # Memory Usage: 14.2 MB, less than 50.11% of Python3 online submissions for Sort Colors.
    # 多个指针同时往前移动
    def sortColors4(self, nums: List[int]) -> None:
        zero_pos, one_pos, two_pos = -1, -1, -1
        for index in range(0, len(nums)):
            if nums[index] == 0:
                zero_pos += 1
                one_pos += 1
                two_pos += 1
                nums[two_pos] = 2
                nums[one_pos] = 1
                nums[zero_pos] = 0
            elif nums[index] == 1:
                one_pos += 1
                two_pos += 1
                nums[two_pos] = 2
                nums[one_pos] = 1
            elif nums[index] == 2:
                two_pos += 1
                nums[two_pos] = 2

    # 两个指针往中间夹
    # Runtime: 20 ms, faster than 99.51% of Python3 online submissions for Sort Colors.
    # Memory Usage: 14.3 MB, less than 22.62% of Python3 online submissions for Sort Colors.
    def sortColors3(self, nums: List[int]) -> None:
        index, zero_pos, two_pos = 0, 0, len(nums) - 1
        while index <= two_pos:
            if nums[index] == 0:
                nums[zero_pos], nums[index] = nums[index], nums[zero_pos]
                zero_pos += 1
                index += 1
            elif nums[index] == 2:
                nums[two_pos], nums[index] = nums[index], nums[two_pos]
                two_pos -= 1
            else:
                index += 1

    # Runtime: 32 ms, faster than 67.99% of Python3 online submissions for Sort Colors.
    # Memory Usage: 14.4 MB, less than 21.84% of Python3 online submissions for Sort Colors.
    # 求出0,1的数量
    def sortColors2(self, nums: List[int]) -> None:
        zero_size, one_size = 0, 0
        for num in nums:
            if num == 0:
                zero_size += 1
                one_size += 1
            elif num == 1:
                one_size += 1
        for i in range(0, len(nums)):
            if i < zero_size:
                nums[i] = 0
            elif i < one_size:
                nums[i] = 1
            else:
                nums[i] = 2

    # Runtime: 40 ms, faster than 10.09% of Python3 online submissions for Sort Colors.
    # Memory Usage: 14.4 MB, less than 21.84% of Python3 online submissions for Sort Colors.
    # 冒泡递归
    def sortColors1(self, nums: List[int]) -> None:
        for index, num in enumerate(nums):
            # 循环结束
            if index == len(nums) - 1: return
            # 当前值小于或等于下一个值,不进行移动
            if num <= nums[index + 1]: continue
            # 移动并检查是否继续向后移动
            self.move(index, nums)

    def move(self, index, nums: List):
        nums[index + 1], nums[index] = nums[index], nums[index + 1]
        if index - 1 < 0: return
        # 当前值小于或等于下一个值,不进行移动
        if nums[index] >= nums[index - 1]: return
        self.move(index - 1, nums)


if __name__ == "__main__":
    # nums = [2, 0, 2, 1, 1, 0]
    nums = [2, 0, 1]
    checker = SortColors()
    checker.sortColors4(nums)
    print(nums)
