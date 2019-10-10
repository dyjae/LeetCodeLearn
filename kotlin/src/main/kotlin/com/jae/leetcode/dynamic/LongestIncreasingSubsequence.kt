package com.jae.leetcode.dynamic

import kotlin.collections.ArrayList

/**
 * @Description: 300. Longest Increasing Subsequence  https://leetcode.com/problems/longest-increasing-subsequence/
 * @Author Jae
 * @Date 2019-10-08 09:33
 **/

object LongestIncreasingSubsequence {

    @JvmStatic
    fun main(args: Array<String>) {
//        println(lengthOfLIS(intArrayOf(10, 9, 2, 5, 3, 7, 101, 18)))
////        println(lengthOfLIS(intArrayOf(10, 9, 2, 5, 3, 4)))
////        println(lengthOfLIS(intArrayOf(2,2)))
        println(lengthOfLIS(intArrayOf(3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12)))
    }


    //Runtime: 168 ms, faster than 82.50% of Kotlin online submissions for Longest Increasing Subsequence.
    //Memory Usage: 32.6 MB, less than 100.00% of Kotlin online submissions for Longest Increasing Subsequence.
//    private fun lengthOfLIS(nums: IntArray): Int {
//        val rs = ArrayList<Int>()
//        nums.forEach { it ->
//            if (rs.isEmpty()) {
//                rs.add(it)
//                return@forEach
//            }
//            val last = rs[rs.size - 1]
//            if (it > last) {
//                rs.add(it)
//                return@forEach
//            }
//            rs[findLastIndexWithIndex(rs, it, 0, rs.size - 1)] = it
//        }
//        return rs.size
//    }
//
//    private fun findLastIndexWithIndex(nums: ArrayList<Int>, num: Int, start: Int, end: Int): Int {
//        if (start == end) return start
//        val mid = start + (end - start) / 2
//        if (mid == 0 && nums[mid] >= num) return mid
//        val midNum = nums[mid]
//        return when {
//            midNum == num -> mid
//            midNum < num -> findLastIndexWithIndex(nums, num, start + 1, end )
//            else -> findLastIndexWithIndex(nums, num, start, end - 1)
//        }
//    }



    //148 ms
    private fun lengthOfLIS(nums: IntArray): Int {
        val list = mutableListOf<Int>()
        var length = 0
        nums.forEach {
            val index = findIndex(list, it, 0, list.size)
            if (index >= list.size) {
                list.add(it)
            } else {
                list[index] = it
            }
            if (index >= length) length++
        }
        return length
    }

    private fun findIndex(list: List<Int>, item: Int, low: Int, high: Int): Int {
        var h = high
        var l = low
        while (l < h) {
            val middle = (l + h) / 2
            if (list[middle] >= item) {
                h = middle
            } else {
                l = middle + 1
            }
        }
        return l
    }

}