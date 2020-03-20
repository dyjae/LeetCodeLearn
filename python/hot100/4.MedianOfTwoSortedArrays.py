#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from typing import List

__author__ = 'Jae'


# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
class MedianOfTwoSortedArrays:

    # 长度为m,n的A，B两个数组分别可以通过i，j 分成两部分

    # 当为偶数时，i+j = m-i + m-j
    # 中位数是  (max(A[i-1],B[j-1]) + min(A[i],B[j])) /2

    # 当为基数时，i+j = m-i + m-j+1
    # 中位数是  max(A[i-1],B[j-1])

    # 边界条件
    # Runtime: 104 ms, faster than 31.99% of Python3 online submissions for Median of Two Sorted Arrays.
    # Memory Usage: 13.2 MB, less than 97.14% of Python3 online submissions for Median of Two Sorted Arrays.
    def find_median_sorted_arrays_4(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 == 0: return self.__findMidlle(nums2)
        if len2 == 0: return self.__findMidlle(nums1)
        if len1 > len2: return self.find_median_sorted_arrays_4(nums2, nums1)
        i_min, i_max, half_len = 0, len1, (len1 + len2 + 1) // 2
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half_len - i
            if i < len1 and nums2[j - 1] > nums1[i]:
                i_min = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                i_max = i_max - 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (len1 + len2) % 2 == 1: return max_left / 1.0

                if i == len1:
                    min_right = nums2[j]
                elif j == len2:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2.0

    # Runtime: 92 ms, faster than 84.22% of Python3 online submissions for Median of Two Sorted Arrays.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
    def find_median_sorted_arrays_binary_search(self, nums1: List[int], nums2: List[int]) -> float:
        # len1 = len(nums1)
        # len2 = len(nums2)
        totalLength = len(nums1) + len(nums2)
        if totalLength % 2 > 0:
            return self.__binary_find(nums1, nums2, totalLength // 2 + 1)
            # return self.__getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, totalLength // 2 + 1)
        else:
            return (self.__binary_find(nums1, nums2, totalLength // 2) +
                    self.__binary_find(nums1, nums2, totalLength // 2 + 1)) / 2
            # return (self.__getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, totalLength // 2 + 1) +
            #         self.__getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, totalLength // 2)) \
            #        / 2

    def __getKth(self, num1, start1, end1, num2, start2, end2, k) -> int:
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2: return self.__getKth(num2, start2, end2, num1, start1, end1, k)
        if len1 == 0: return num2[start2 + k - 1]
        if k == 1: return min(num1[start1], num2[start2])

        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1

        if num1[i] > num2[j]:
            return self.__getKth(num1, start1, end1, num2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.__getKth(num1, i + 1, end1, num2, j, end2, k - (i - start1 + 1))

    def __binary_find(self, nums1: List[int], nums2: List[int], k) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2: return self.__binary_find(nums2, nums1, k)
        if len1 == 0: return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0]) * 1.0
        mid = k // 2
        temp1, temp2 = nums1, nums2
        # 取参与比较的位置
        i = min(len1, mid) - 1
        j = min(len2, mid) - 1
        if temp1[i] > temp2[j]:
            return self.__binary_find(temp1, temp2[j + 1:], k - j - 1)
        else:
            return self.__binary_find(temp1[i + 1:], temp2, k - i - 1)

    # Runtime: 100 ms, faster than 42.07% of Python3 online submissions for Median of Two Sorted Arrays.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays。
    # 同时遍历求中位数
    def find_median_sorted_arrays_mid(self, nums1: List[int], nums2: List[int]) -> float:
        left, right, index1, index2 = -1, -1, 0, 0
        len1, len2 = len(nums1), len(nums2)
        totalLen = len1 + len2
        for i in range(0, (totalLen // 2) + 1):
            if index1 < len1 and (index2 >= len2 or nums1[index1] < nums2[index2]):
                left, right = right, nums1[index1]
                index1 += 1
            elif index2 < len2:
                left, right = right, nums2[index2]
                index2 += 1
        if totalLen % 2 > 0:
            return right / 1.0
        else:
            return (right + left) / 2.0

    # Runtime: 100 ms, faster than 41.63% of Python3 online submissions for Median of Two Sorted Arrays.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
    # 合并两个数组，取中位数
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, count = 0, 0, 0
        m1Length, m2Length = len(nums1), len(nums2)
        totalLen = m1Length + m2Length
        nums = []
        while count < totalLen:
            if i == m1Length:  # nums1已经取完
                while j < m2Length:
                    nums.append(nums2[j])
                    count += 1
                    j += 1
                continue
            if j == m2Length:  # num2已经取完
                while i < m1Length:
                    nums.append(nums1[i])
                    count += 1
                    i += 1
                continue
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            count += 1
        return self.__findMidlle(nums)

    def __findMidlle(self, nums):
        length = len(nums)
        if length % 2 == 0:  # 偶数
            return (nums[length // 2 - 1] + nums[length // 2]) / 2.0
        else:
            return nums[length // 2] / 1.0


if __name__ == "__main__":
    num1 = [1, 3]
    num2 = [2]
    # num1 = [1, 2]
    # num2 = [3, 4]

    # num1 = [2]
    # num2 = []
    mta = MedianOfTwoSortedArrays()
    print(mta.find_median_sorted_arrays(num1, num2))
    print(mta.find_median_sorted_arrays_mid(num1, num2))
    print(mta.find_median_sorted_arrays_binary_search(num1, num2))
    print(mta.find_median_sorted_arrays_4(num1, num2))
