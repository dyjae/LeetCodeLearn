#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 78.Subsets.py
# DATE : 2021/1/5 08:55

__author__ = 'Jae'

# https://leetcode.com/problems/subsets/
from typing import List


class Subsets:

    # dfs
    # 同 subsets1
    def subsets6(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], path + [nums[i]], ret)

    # 同 subsets2
    def subsets5(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    # 位运算
    # 有多少个数,表示二进制有多少位
    # 遍历从0到最大数,可以遍历到所有位的情况,为1就是有该位的数
    # 注意 位与运算 要用&
    # Runtime: 28 ms, faster than 94.23% of Python3 online submissions for Subsets.
    # Memory Usage: 14.6 MB, less than 21.62% of Python3 online submissions for Subsets.
    def subsets4(self, nums: List[int]) -> List[List[int]]:
        rs = []
        length = len(nums)
        totalNum = 1 << length
        for num in range(totalNum):
            temp = []
            pos = num
            count = 0
            while pos != 0:
                if (pos & 1) == 1:
                    temp.append(nums[count])
                count += 1
                pos = pos >> 1
            rs.append(temp)
        return rs

    # Runtime: 28 ms, faster than 94.13% of Python3 online submissions for Subsets.
    # Memory Usage: 14.6 MB, less than 19.53% of Python3 online submissions for Subsets.
    # 回溯法
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        self.rs = []
        self.__get_rs(nums, 0, [])
        return self.rs

    def __get_rs(self, nums: List[int], start: int, temp: List[int]):
        self.rs.append(temp[:])
        for index in range(start, len(nums)):
            temp.append(nums[index])
            # 这里是要从当前位置的下一个位子开始遍历,而不是start的位置开始,start开始就会重新遍历很多
            self.__get_rs(nums, index + 1, temp)
            temp.pop()

    # Runtime: 40 ms, faster than 16.51% of Python3 online submissions for Subsets.
    # Memory Usage: 14.4 MB, less than 46.26% of Python3 online submissions for Subsets.
    # 遍历每一个数
    # 1 1
    # 2 2 12
    # 3 3 13 23 123
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        rs = [[]]
        for num in nums:
            temp = []
            for item in rs:
                if item is None or len(item) == 0:
                    temp.append([num])
                    continue
                newList = item[:]
                newList.append(num)
                temp.append(newList)
            for item in temp:
                rs.append(item)
        return rs

    # Runtime: 36 ms, faster than 52.01% of Python3 online submissions for Subsets.
    # Memory Usage: 14.3 MB, less than 67.21% of Python3 online submissions for Subsets.
    # 每次循环一层
    # 1,2,3
    # 12 13 23
    # 123
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        rs = [[]]
        for i in nums:
            rs.append([i])
        ans = [[i] for i in nums]
        nLen = len(nums)
        for i in range(nLen):
            temp = []
            for item in ans:
                for num in nums:
                    if item is not None and len(item) > 0 and item[-1] >= num: continue
                    newList = item[:]
                    newList.append(num)
                    temp.append(newList)
                    rs.append(newList)
            ans = temp
        return list(rs)


if __name__ == "__main__":
    nums = [1, 2, 3]
    # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    checker = Subsets()
    print(checker.subsets1(nums))
    print(checker.subsets2(nums))
    print(checker.subsets3(nums))
    print(checker.subsets4(nums))
