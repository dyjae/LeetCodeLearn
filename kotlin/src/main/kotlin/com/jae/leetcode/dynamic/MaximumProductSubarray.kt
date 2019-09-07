package com.jae.leetcode.dynamic


/**
 * @Description: https://leetcode.com/problems/maximum-product-subarray   152. Maximum Product Subarray
 * @Author Jae
 * @Date 2019-09-07 11:19
 **/
object MaximumProductSubarray {

    @JvmStatic
    fun main(args: Array<String>) {
        println(maxProduct(intArrayOf(2, 3, -2, 4)))
        println(maxProduct(intArrayOf(-2, 0, -1)))
    }

    //动态规划
    //Runtime: 140 ms, faster than 100.00% of Kotlin online submissions for Maximum Product Subarray.
    //Memory Usage: 33.5 MB, less than 100.00% of Kotlin online submissions for Maximum Product Subarray.
    fun maxProduct(nums: IntArray): Int {
        val dp = Array(2) { IntArray(2) { nums[0] } }
        var rs = nums[0]
        for (i in 1 until nums.size) {
            val index = (i - 1) % 2
            val index2 = i % 2
            val n1 = dp[index][0] * nums[i]
            val n2 = dp[index][1] * nums[i]
            val n3 = nums[i]
            dp[index2][0] = maxOf(n1, n2, n3)
            dp[index2][1] = minOf(n1, n2, n3)
            rs = maxOf(dp[index2][0], rs)
        }
        return rs
    }

    //暴力求解
//    fun maxProduct(nums: IntArray): Int {
//        var max = Int.MIN_VALUE
//        for (i in 0 until nums.size) {
//            for (j in i until nums.size) {
//                val subNums = nums.copyOfRange(i, j + 1)
//                val maxValue = subNums.fold(1) { acc, it ->
//                    acc * it
//                }
//                max = maxOf(max, maxValue)
//            }
//        }
//        return max
//    }


}
