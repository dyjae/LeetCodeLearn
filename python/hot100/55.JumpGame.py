#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 55.JumpGame.py
# DATE : 2020/10/21 10:14

__author__ = 'Jae'

# https://leetcode.com/problems/jump-game/
from typing import List


class JumpGame:

    # 前面点能到达的最大距离是否能到当前点
    # Runtime: 88 ms, faster than 64.25% of Python3 online submissions for Jump Game.
    # Memory Usage: 15.9 MB, less than 99.99% of Python3 online submissions for Jump Game.
    def canJump4(self, nums: List[int]) -> bool:
        maxVal = 0
        for index, num in enumerate(nums):
            if maxVal < index:
                return False
            maxVal = max(maxVal, num + index)
        return True

    # 从终点往回找
    # BUG TIME LIMIT
    def canJump3(self, nums: List[int]) -> bool:
        position = len(nums) - 1
        while position != 0:
            isUpdate = False
            for index in range(0, position):
                if nums[index] >= position - index:
                    isUpdate = True
                    position = index
                    break
            if not isUpdate: return False
        return True

    # 贪婪算法
    # 每次取最大
    # 会遇到前面取最大,后面数反而小(为0)导致没有办法走完的情况  BUG
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1: return True
        endPos = 0
        while endPos < length:
            if nums[endPos] == 0: return False
            endPos += nums[endPos]
        return True


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    checked = JumpGame()
    print(checked.canJump(nums))
    # print(checked.canJump2(nums))
    print(checked.canJump3(nums))
    print(checked.canJump4(nums))
