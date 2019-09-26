package com.jae.leetcode.dynamic

/**
 * @Description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
 * @Author Jae
 * @Date 2019-09-10 09:52
 **/

object BestTimeToBuyAndSellStockIV {

    @JvmStatic
    fun main(args: Array<String>) {
        println(maxProfit(2, intArrayOf(2,4,1)))
    }


    fun maxProfit(k: Int, prices: IntArray): Int {

        if (k > prices.size / 2) {
            var max = 0
            for (i in 1 until prices.size) {
                if (prices[i] > prices[i - 1])
                    max += prices[i] - prices[i - 1]
            }
            return max
        }

        val dp = Array(prices.size) { Array(k + 1) { Array(2) { 0 } } }
        for (i in 0 until prices.size) {
            for (j in k downTo 1) {
                if (i == 0) {
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                }
                dp[i][j][0] = maxOf(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = maxOf(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
            }
        }
        return dp[prices.size - 1][k][0]
    }


    //Runtime: 180 ms, faster than 70.59% of Kotlin online submissions for Best Time to Buy and Sell Stock IV.
//Memory Usage: 33.9 MB, less than 100.00% of Kotlin online submissions for Best Time to Buy and Sell Stock IV.
//    fun maxProfit(k: Int, prices: IntArray): Int {
//        val length = prices.size
//        if (length <= 1) return 0
//        if (k >= length / 2) { //超过一半的天数有交易
//            var maxPro = 0
//            for (i in 1 until length) {//贪婪交易
//                if (prices[i] > prices[i - 1])
//                    maxPro += prices[i] - prices[i - 1]
//            }
//            return maxPro
//        }
//        val dp = Array(k + 1) { IntArray(length) }
//        for (i in 1..k) {
//            var localMax = dp[i - 1][0] - prices[0]  //第一天买入
//            for (j in 1 until length) {
//                dp[i][j] = maxOf(dp[i][j - 1], prices[j] + localMax) //第j天卖出和不交易，最大利润
//                localMax = maxOf(localMax, dp[i - 1][j] - prices[j]) //买入和不交易最大利润
//            }
//        }
//        return dp[k][length - 1]
//    }

//    //160 ms
//    fun maxProfit(k: Int, prices: IntArray): Int {
//        if (k == 0) {
//            return 0
//        }
//        if (k > prices.size) {
//            return maxProfitAny(prices)
//        }
//        val buy = IntArray(k) { Int.MIN_VALUE }
//        val sell = IntArray(k) { 0 }
//        prices.forEach { p ->
//            for (i in 0 until k) {
//                buy[i] = if (i == 0) {
//                    maxOf(buy[i], -p)
//                } else {
//                    maxOf(buy[i], sell[i - 1] - p)
//                }
//                sell[i] = maxOf(sell[i], buy[i] + p)
//            }
//        }
//        return sell[k - 1]
//    }
//
//    private fun maxProfitAny(prices: IntArray): Int {
//        var max = 0
//        for (i in 1 until prices.size) {
//            if (prices[i] > prices[i - 1])
//                max += prices[i] - prices[i - 1]
//        }
//        return max
//    }

//    fun maxProfit(k: Int, prices: IntArray): Int {
//        if (prices.isEmpty()) return 0
//        val rs = Array(k + 1) { Array(prices.size) { 0 } }
//        var maxProf = 0
//        for (kk in 1..k) {
//            var tempMax = rs[kk - 1][0] - prices[0]
//            for (i in 1 until prices.size) {
//                rs[kk][i] = maxOf(rs[kk][i - 1], prices[i] + tempMax) //上一天交易完k次  和  第i日卖掉+上次k-1买的利润最大
//                tempMax = maxOf(tempMax, rs[kk - 1][i] - prices[i]) //最后一次买入的收益  和 第i日买入，利润最大值
//                maxProf = maxOf(rs[kk][i], maxProf)   // 第i日交易完利润 和  其他利润最大比较
//            }
//        }
//        return maxProf
//    }
}