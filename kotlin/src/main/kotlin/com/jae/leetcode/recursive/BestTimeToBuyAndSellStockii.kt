package com.jae.leetcode.recursive

/**
 * @Description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
 * @Author yj
 * @Date 2019-08-12 18:00
 **/
fun main(args: Array<String>) {
    println(maxProfit(intArrayOf(7, 6, 4, 3, 1)))
}

//Runtime: 172 ms, faster than 94.23% of Kotlin online submissions for Best Time to Buy and Sell Stock II.
//Memory Usage: 36.1 MB, less than 100.00% of Kotlin online submissions for Best Time to Buy and Sell Stock II.
fun maxProfit(prices: IntArray): Int {
    var money = 0
    prices.forEachIndexed { index, value ->
        if (prices.size - 1 == index) return money
        if (prices[index + 1] > value) money += prices[index + 1] - value
    }
    return money
}

//164
//fun maxProfit(prices: IntArray): Int {
//    var indexSize = prices.size - 1
//    var maxProfit = 0
//
//    for(i in 0 until indexSize ){
//        if(prices[i] < prices[i + 1]){
//            maxProfit += prices[i + 1] - prices[i]
//        }
//    }
//
//    return maxProfit
//}