package com.jae.leetcode.dynamic

/**
 * @Description:
 * @Author Jae
 * @Date 2019-09-19 09:54
 **/
object BestTimeToBuyAndSellStockWithCooldown {
    @JvmStatic
    fun main(args: Array<String>) {
        println(maxProfit(intArrayOf(1,2,3,0,2)))
    }

    //Runtime: 140 ms, faster than 100.00% of Kotlin online submissions for Best Time to Buy and Sell Stock with Cooldown.
    //Memory Usage: 32.5 MB, less than 100.00% of Kotlin online submissions for Best Time to Buy and Sell Stock with Cooldown.
    private fun maxProfit(prices: IntArray): Int {
        var hold = Int.MIN_VALUE
        var none = 0
        var preSell = 0
        for (i in 0 until prices.size) {
            val temp = none
            hold = maxOf(hold, preSell - prices[i])
            none = maxOf(hold + prices[i], none)
            preSell = temp
        }
        return none
    }
}
