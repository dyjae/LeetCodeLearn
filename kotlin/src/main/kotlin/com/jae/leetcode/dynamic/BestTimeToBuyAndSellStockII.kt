package com.jae.leetcode.dynamic

/**
 * @Description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
 * @Author Jae
 * @Date 2019-09-18 09:49
 **/
object BestTimeToBuyAndSellStockII {
    @JvmStatic
    fun main(args: Array<String>) {
        println(maxProfit(intArrayOf(7, 1, 5, 3, 6, 4)))
        println(maxProfit(intArrayOf(1, 2, 3, 4, 5)))
        println(maxProfit(intArrayOf(7, 6, 4, 3, 1)))
    }

    //Runtime: 180 ms, faster than 68.64% of Kotlin online submissions for Best Time to Buy and Sell Stock II.
    //Memory Usage: 36.1 MB, less than 100.00% of Kotlin online submissions for Best Time to Buy and Sell Stock II.
    fun maxProfit(prices: IntArray): Int {
        if (prices.isEmpty()) return 0
        val n = prices.size
        val dp = IntArray(n)
        dp[n - 1] = 0
        for (i in n - 1 downTo 1) {
            dp[i - 1] = maxOf(prices[i] - prices[i - 1], 0) + dp[i]
        }
        return dp[0]
    }
}