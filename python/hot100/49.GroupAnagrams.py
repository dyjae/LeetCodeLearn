#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 49.GroupAnagrams.py
# DATE : 2020/10/10 09:39

__author__ = 'Jae'

import collections
from typing import List


# https://leetcode.com/problems/group-anagrams/
class GroupAnagrams:

    # 算术基本定理，又称为正整数的唯一分解定理，即：每个大于1的自然数，要么本身就是质数，要么可以写为2个以上的质数的积，而且这些质因子按大小排列之后，写法仅有一种方式
    # Runtime: 100 ms, faster than 75.63% of Python3 online submissions for Group Anagrams.
    # Memory Usage: 16.9 MB, less than 6.56% of Python3 online submissions for Group Anagrams.
    # 时间复杂度：O（n * K），K 是字符串的最长长度。
    # 空间复杂度：O（NK），用来存储结果。
    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        rs = collections.defaultdict(list)
        # ord() 求ascall码
        orda = ord('a')
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103)
        for vstr in strs:
            key = 1
            for vchar in vstr:
                key *= primes[ord(vchar) - orda]
            if rs.__contains__(key):
                rs[key].append(vstr)
            else:
                rs[key] = [vstr]
        return list(rs.values())

    # 将每一排序后放入字典,最后字典的value值就是需要的结果
    # Runtime: 96 ms, faster than 87.22% of Python3 online submissions for Group Anagrams.
    # Memory Usage: 18 MB, less than 6.40% of Python3 online submissions for Group Anagrams.
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # 生成以list为key的默认dict
        rsmap = collections.defaultdict(list)
        for str in strs:
            # tuple 转换成元组
            rsmap[tuple(sorted(str))].append(str)
        # list 将dict_values 转换成list
        return list(rsmap.values())

    # 暴力求解
    # 循环两两比较长度和是否相等,使用一个布尔数组判断是否已添加
    # 使用map判断字符串是否相等
    # 会超时
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checked = [False for _ in strs]
        length = len(strs)
        rs = []
        for index, item in enumerate(strs):
            if checked[index]: continue
            temp = [item]
            for i in range(index + 1, length):
                if self.__equal(item, strs[i]):
                    temp.append(strs[i])
                    checked[i] = True
            rs.append(temp)
        return rs

    def __equal(self, str1, str2) -> bool:
        tempMap = dict()
        self.__addMap(tempMap, str1)
        self.__reduceMap(tempMap, str2)
        # 检查是否每一个字符是否为0
        for charNum in tempMap.values():
            if charNum != 0: return False
        return True

    def __addMap(self, map, str):
        for index, item in enumerate(str):
            value = map.get(item)
            if value is None:
                value = 1
            else:
                value += 1
            map[item] = value

    def __reduceMap(self, map, str):
        for index, item in enumerate(str):
            value = map.get(item)
            if value is None:
                value = -1
            else:
                value -= 1
            map[item] = value


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = ["abbbbbbbbbbb", "aaaaaaaaaaab"]
    checked = GroupAnagrams()
    print(checked.groupAnagrams(strs))
    print(checked.groupAnagrams(strs2))
    print(checked.groupAnagrams2(strs2))
    print(checked.groupAnagrams3(strs2))
