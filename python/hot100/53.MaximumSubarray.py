#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 53.MaximumSubarray.py
# DATE : 2020/10/13 09:41

__author__ = 'Jae'

import sys
from typing import List


# https://leetcode.com/problems/maximum-subarray/
class MaximumSubarray:
    min_value = -sys.maxsize - 1

    # 拿出一个变量保存最大值,然后遍历取大于0的和,和小于0时就清0
    def maxSubArray5(self, nums: List[int]) -> int:
        maxi = max(nums)
        n = len(nums)
        ret = 0
        for i in range(n):
            ret += nums[i]
            maxi = max(maxi, ret)
            if ret < 0:
                ret = 0
        return maxi

    # dp
    # 实际和前面解法一样,但是没有单独开辟空间
    def maxSubArray4(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            diff = nums[i] + nums[i + 1]
            if diff > nums[i + 1]:
                nums[i + 1] = diff
        return max(nums)

    # dp
    # 对于i结尾的数 dp[i]表示前i位数最大的和   dp[i] = max(nums[i],dp[i-1]+nums[i])
    # Runtime: 68 ms, faster than 59.01% of Python3 online submissions for Maximum Subarray.
    # Memory Usage: 14.8 MB, less than 84.56% of Python3 online submissions for Maximum Subarray.
    def maxSubArray3(self, nums: List[int]) -> int:
        maxVal, dp = nums[0], nums[0]
        for index in range(1, len(nums)):
            dp = max(nums[index], dp + nums[index])
            maxVal = max(dp, maxVal)
        return maxVal

    # 假dp 实际和解法一是一样的,会超时
    # dp [ i ] [ len + 1 ] = dp[ i ] [ len ] + nums [ i + len - 1 ]。
    # i为下标 len为长度
    # 因为最后比较的是
    def maxSubArray2(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0 for _ in range(length)]
        maxVal = self.min_value
        for lenIndex in range(1, length + 1):
            for i in range(0, length - lenIndex + 1):
                dp[i] = dp[i] + nums[i + lenIndex - 1]
                if dp[i] > maxVal:
                    maxVal = dp[i]
        return maxVal

    # 暴力解法, 循环
    # 会超时
    def maxSubArray(self, nums: List[int]) -> int:
        maxTemp = self.min_value
        for index in range(len(nums)):
            maxVal = self.__maxNum(nums[index:])
            maxTemp = max(maxVal, maxTemp)
        return maxTemp

    def __maxNum(self, nums: List[int]):
        maxTemp = self.min_value
        temp = 0
        for num in nums:
            temp += num
            maxTemp = max(maxTemp, temp)
        return maxTemp


if __name__ == "__main__":
    cheked = MaximumSubarray()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums2 = [-1]
    print(cheked.maxSubArray(nums))
    print(cheked.maxSubArray(nums2))
    print(cheked.maxSubArray2(nums))
    print(cheked.maxSubArray2(nums2))
    print(cheked.maxSubArray3(nums2))
