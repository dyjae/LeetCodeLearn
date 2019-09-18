package com.jae.leetcode.dynamic

/**
 * @Description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 * @Author Jae
 * @Date 2019-09-18 09:24
 **/

object BestTimeToBuyAndSellStock {

    @JvmStatic
    fun main(args: Array<String>) {
        println(maxProfit(intArrayOf(7, 1, 5, 3, 6, 4)))
    }

    //Runtime: 180 ms, faster than 70.19% of Kotlin online submissions for Best Time to Buy and Sell Stock.
    //Memory Usage: 37.8 MB, less than 100.00% of Kotlin online submissions for Best Time to Buy and Sell Stock.
    fun maxProfit(prices: IntArray): Int {
        var minPrice = Int.MAX_VALUE
        var maxProfit = 0
        prices.forEach { price ->
            if (price < minPrice) {
                minPrice = price
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice
            }
        }
        return maxProfit
    }
}

