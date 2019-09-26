package com.jae.leetcode.dynamic

/**
 * @Description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
 * @Author Jae
 * @Date 2019-09-26 09:17
 **/

object BestTimeToBuyAndSellStockwithTransactionFee {
    @JvmStatic
    fun main(args: Array<String>) {
        println(maxProfit(intArrayOf(1, 3, 2, 8, 4, 9), 2))
    }

    //Runtime: 364 ms, faster than 83.33% of Kotlin online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
    //Memory Usage: 49.1 MB, less than 100.00% of Kotlin online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
    private fun maxProfit(prices: IntArray, fee: Int): Int {
        var hold = Int.MIN_VALUE
        var none = 0

        for (i in 0 until prices.size) {
            hold = maxOf(hold, none - prices[i] - fee)
            none = maxOf(none, hold + prices[i])
        }
        return none
    }


    /*
   Keep two data: maxProfit records max profit so far.
   lastSellPos keeps until position i, the last sell position.

   for each position i,
   maxProfit = Math.max(
       maxProfit, // no buy & sell since lastSellPos
       maxProfit + (prices[i] - prices[lastSellPos]), // sell at i rather than at lastSellPos, also update lastSellPos
       maxProfit + maxProfitWithSingleBuySellAfterLastSellPos // after lastSellPos, make one more profitable buy & sell, update lastSellPos
   )
   */
    //348
//    fun maxProfit(prices: IntArray, fee: Int): Int {
//        if (prices.isEmpty()) return 0
//
//        // TODO use Long to avoid int overflow?
//        var maxProfit = 0
//        var lastSellPos = -1
//        var nextBuyPos = 0 // invariant: nextBuyPos > lastSellPos
//
//        for (i in 0 until prices.size) {
//            val buyNewSellNowProfit = prices[i] - prices[nextBuyPos] - fee
//            val buySameSellNowProfit = if (lastSellPos < 0) 0 else prices[i] - prices[lastSellPos]
//            if (buyNewSellNowProfit > 0 || buySameSellNowProfit > 0) {
//                lastSellPos = i
//                nextBuyPos = i + 1
//                maxProfit += Math.max(buyNewSellNowProfit, buySameSellNowProfit)
//            } else {
//                if (prices[i] < prices[nextBuyPos]) nextBuyPos = i
//            }
//        }
//
//        return maxProfit
//    }

}