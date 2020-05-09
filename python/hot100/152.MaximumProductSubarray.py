#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

import sys
from typing import List


class MaximumProductSubarray:

    # DP
    # 每个位置最大值等于 上一个位子最大值或最小值乘以当前位置的大者
    # 要不停计算最大值与当前最大值比较，最大最小值要与当前值比较
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        min_p = max_p = nums[0]
        global_mp = nums[0]

        for num in nums[1:]:
            tmp = min_p
            min_p = min(num, min_p * num, max_p * num)
            max_p = max(num, max_p * num, tmp * num)
            global_mp = max(global_mp, max_p)
        return global_mp

    # DP
    # 每个位置最大值等于 上一个位子最大值或最小值乘以当前位置的大者
    # Runtime: 52 ms, faster than 82.84% of Python3 online submissions for Maximum Product Subarray.
    # Memory Usage: 14.2 MB, less than 17.24% of Python3 online submissions for Maximum Product Subarray.
    def maxProduct2(self, nums: List[int]) -> int:
        length = len(nums)
        lastMaxNum = 1
        lastMinNum = 1
        maxNum = -sys.maxsize - 1
        for i in range(length):
            if nums[i] < 0:
                lastMaxNum, lastMinNum = lastMinNum, lastMaxNum
            lastMaxNum = max(lastMaxNum * nums[i], nums[i])
            lastMinNum = min(lastMinNum * nums[i], nums[i])
            maxNum = max(lastMaxNum, maxNum)
        return maxNum

    # 暴力求解
    # Timeout
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0: return 0
        maxNum = nums[0]
        for i in range(length):
            newMax = self.__getMaxProduct(nums[i + 1:length], nums[i])
            maxNum = max(maxNum, newMax)
        return maxNum

    def __getMaxProduct(self, nums: List[int], maxNum):
        if len(nums) == 0: return maxNum
        newNum = nums[0] * maxNum
        maxNum = max(newNum, maxNum)
        if len(nums) == 1:
            return maxNum
        else:
            newNum2 = self.__getMaxProduct(nums[1:len(nums)], newNum)
            maxNum = max(maxNum, newNum2)
        return maxNum


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    # nums = [-2, 0, -1]
    check = MaximumProductSubarray()
    print(check.maxProduct(nums))
    print(check.maxProduct2(nums))
