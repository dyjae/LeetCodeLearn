#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from typing import List


# https://leetcode.com/problems/jump-game-ii/
class JumpGameII:

    # fast
    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        if len(set(nums)) == 1: return (n - 1) // nums[0] + [1, 0][(n - 1) % nums[0] == 0]
        idx = len(nums) - 1  # starts from the end, idx is the current position
        step = 0
        while idx > 0:
            step += 1
            for i in range(idx):
                if i + nums[i] >= idx:
                    idx = i
                    break
        return step

    # 贪心算法
    # Runtime: 96 ms, faster than 76.53% of Python3 online submissions for Jump Game II.
    # Memory Usage: 16.1 MB, less than 8.33% of Python3 online submissions for Jump Game II.
    def jump1(self, nums: List[int]) -> int:
        end = 0
        maxPosition = 0
        step = 0
        for i, num in enumerate(nums):
            if end >= len(nums) - 1:
                return step
            maxPosition = max(maxPosition, num + i)
            if i == end:
                end = maxPosition
                step += 1
        return step


if __name__ == "__main__":
    checker = JumpGameII()
    array = [2, 3, 1, 1, 4]
    array2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
    array3 = [2, 3, 0, 1, 4]
    print(checker.jump1(array))
    # print(checker.jump1(array2))
    # print(checker.jump1(array3))
