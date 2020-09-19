#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from typing import List


class Permutations:

    # 函数
    def permute4(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return permutations(nums)

    # https://leetcode.com/problems/permutations/
    # https://leetcode.wang/leetCode-46-Permutations.html
    # Runtime: 36 ms, faster than 90.88% of Python3 online submissions for Permutations.
    # Memory Usage: 13.9 MB, less than 67.20% of Python3 online submissions for Permutations.
    def permute3(self, nums: List[int]) -> List[List[int]]:
        rs = []
        self.__upset(nums, 0, rs)
        return rs

    def __upset(self, nums: List[int], index: int, rs: List[List[int]]):
        if index >= len(nums):
            rs.append(nums.copy())
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.__upset(nums, index + 1, rs)
            nums[i], nums[index] = nums[index], nums[i]

    # 回溯 DFS
    # Runtime: 32 ms, faster than 97.63% of Python3 online submissions for Permutations.
    # Memory Usage: 14.1 MB, less than 30.71% of Python3 online submissions for Permutations.
    def permute2(self, nums: List[int]) -> List[List[int]]:
        rs = []
        self.__back_track(nums, [], rs)
        return rs

    def __back_track(self, nums: List[int], temp: List[int], rs: List[List[int]]):
        if len(temp) == len(nums):
            rs.append(temp.copy())
            return
        for item in nums:
            if temp.__contains__(item): continue
            temp.append(item)
            self.__back_track(nums, temp, rs)
            temp.pop()

    # 暴力求解，多重循环，通过在已有数字的间隙中插入新数字
    # Runtime: 40 ms, faster than 77.80% of Python3 online submissions for Permutations.
    # Memory Usage: 13.9 MB, less than 72.33% of Python3 online submissions for Permutations.
    def permute(self, nums: List[int]) -> List[List[int]]:
        rs = [[]]
        for i in range(0, len(nums)):
            currentSize = len(rs)
            for j in range(0, currentSize):
                for k in range(0, i + 1):
                    temp = rs[j].copy()
                    temp.insert(k, nums[i])
                    rs.append(temp)
            # 移除上一步过程值
            for j in range(0, currentSize):
                rs.remove(rs[0])
        return rs

    def permute5(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])  ###insert n
            perms = new_perms
        return perms


if __name__ == "__main__":
    list = [1, 2, 3]
    check = Permutations()
    print(check.permute(list))
    print(check.permute5(list))
    print(check.permute2(list))
    print(check.permute3(list))
    print(check.permute4(list))
