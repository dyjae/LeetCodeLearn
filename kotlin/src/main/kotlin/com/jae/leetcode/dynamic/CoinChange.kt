package com.jae.leetcode.dynamic

/**
 * @Description: 322. Coin Change https://leetcode.com/problems/coin-change/
 * @Author Jae
 * @Date 2019-10-16 09:39
 **/

object CoinChange {

    @JvmStatic
    fun main(args: Array<String>) {
        println(coinChange(intArrayOf(1, 2, 5), 11))
        println(coinChange(intArrayOf(2), 3))
    }

    //Runtime: 160 ms, faster than 91.38% of Kotlin online submissions for Coin Change.
    //Memory Usage: 35.1 MB, less than 100.00% of Kotlin online submissions for Coin Change.
    fun coinChange(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount + 1) { amount + 1 }
        dp[0] = 0
        for (i in 1..amount) {
            coins.forEach { coin ->
                if (i >= coin) {
                    dp[i] = minOf(dp[i], dp[i - coin] + 1)
                }
            }
        }
        return if (dp[amount] > amount) -1 else dp[amount]
    }
}