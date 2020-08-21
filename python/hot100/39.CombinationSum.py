#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from typing import List


class CombinationSum:

    # 动态规划
    # 直接排除了重复情况
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {0: [[]]}
        candidates.sort()
        for c in candidates:
            for t in range(c, target + 1):
                if (t - c) in dp:
                    if t not in dp:
                        dp[t] = []
                    for comb_t_m_c in dp[t - c]:
                        dp[t].append(comb_t_m_c + [c])
        return dp[target] if target in dp else []

    # 动态规划
    # opt[target]= opt[target-nums[i]] + nums[i]
    # 去重
    # Runtime: 224 ms, faster than 12.33% of Python3 online submissions for Combination Sum.
    # Memory Usage: 20 MB, less than 5.03% of Python3 online submissions for Combination Sum.
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        opts = dict()
        for i in range(0, target + 1):
            opts[i] = []
            for index in range(0, len(candidates)):
                num = candidates[index]
                if i == num:
                    opts[i].append([num])
                elif i > num:
                    for item in opts[i - num]:
                        newItem = item.copy()
                        newItem.append(num)
                        opts[i].append(newItem)
        # 去重
        rsSet = set()
        for item in opts[target]:
            item.sort()
            rsSet.add(self.__join_list(item))

        return self.__split_set(rsSet)

    def __split_set(self, set: set):
        list = []
        for item in set:
            splitItem = item.split(',')
            tempList = []
            for item1 in splitItem:
                tempList.append(int(item1))
            list.append(tempList)
        return list

    def __join_list(self, list: List[int]):
        strs = ""
        for index, item in enumerate(list):
            if index == len(list) - 1:
                strs += str(item)
            else:
                strs += str(item) + ','
        return strs

    # 回溯法
    # 每个数都从当前位置往后加，直到相等或超出
    # Runtime: 88 ms, faster than 61.47% of Python3 online submissions for Combination Sum.
    # Memory Usage: 13.6 MB, less than 98.86% of Python3 online submissions for Combination Sum.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rsList = []
        tempList = []
        self.__findCombination(rsList, tempList, candidates, target, 0)
        return rsList

    def __findCombination(self, rsList: List[List[int]], tempList: List[int], candidates: List[int], target: int,
                          start: int, ):
        # 符合条件
        if target == 0: return rsList.append(tempList.copy())
        for i in range(start, len(candidates)):
            tempList.append(candidates[i])
            nextVal = target - candidates[i]
            if nextVal < 0:
                tempList.pop()
                return
            self.__findCombination(rsList, tempList, candidates, nextVal, i)
            tempList.pop()


if __name__ == "__main__":
    check = CombinationSum()
    candidates = [2, 3, 6, 7]
    target = 7
    # [7],
    # [2,2,3]
    rs = check.combinationSum(candidates, target)
    print(rs)

    print(check.combinationSum2(candidates, target))
    print(check.combinationSum3(candidates, target))
