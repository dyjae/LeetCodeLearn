package com.jae.leetcode.dynamic

/**
 * @Description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
 * @Author Jae
 * @Date 2019-09-19 09:38
 **/
object BestTimeToBuyAndSellStockIII {
    @JvmStatic
    fun main(args: Array<String>) {
        println(maxProfit(intArrayOf(3, 3, 5, 0, 0, 3, 1, 4)))
    }

    //Runtime: 176 ms, faster than 94.59% of Kotlin online submissions for Best Time to Buy and Sell Stock III.
    //Memory Usage: 36.3 MB, less than 100.00% of Kotlin online submissions for Best Time to Buy and Sell Stock III.
    fun maxProfit(prices: IntArray): Int {
        if (prices.isEmpty()) return 0
        val k = 2
        var maxProfit = 0
        val dp = Array(k + 1) { IntArray(prices.size) { 0 } }
        for (kk in 1..k) {
            var tempMax = dp[kk - 1][0] - prices[0] //买入
            for (i in 1 until prices.size) {
                dp[kk][i] = maxOf(dp[kk][i - 1], tempMax + prices[i])
                tempMax = maxOf(tempMax, dp[kk - 1][i] - prices[i])
                maxProfit = maxOf(maxProfit, dp[kk][i])
            }
        }
        return maxProfit
    }

}