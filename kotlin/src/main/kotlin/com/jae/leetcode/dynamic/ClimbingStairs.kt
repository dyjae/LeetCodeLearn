package com.jae.leetcode.dynamic

import kotlin.math.pow
import kotlin.math.sqrt

/**
 * @Description:    https://leetcode.com/problems/climbing-stairs
 * @Author Jae
 * @Date 2019-09-03 09:34
 **/

fun main() {
    println(climbStairs(45))
}


//Runtime: 124 ms, faster than 50.32% of Kotlin online submissions for Climbing Stairs.
//Memory Usage: 31.3 MB, less than 100.00% of Kotlin online submissions for Climbing Stairs.
//fun climbStairs(n: Int): Int {
//    return climb(n, HashMap<Int, Int>().toMutableMap())
//}
//
//fun climb(n: Int, temp: MutableMap<Int, Int?>): Int {
//    if (n <= 1) return 1
//    val tm = temp[n] ?: climb(n - 1, temp) + climb(n - 2, temp)
//    temp[n] = tm
//    return tm
//}


//Dynamic Programming
//fun climbStairs(n: Int): Int {
//    if (n == 1) {
//        return 1
//    }
//    val dp = IntArray(n + 1)
//    dp[1] = 1
//    dp[2] = 2
//    for (i in 3..n) {
//        dp[i] = dp[i - 1] + dp[i - 2]
//    }
//    return dp[n]
//}


//100
fun climbStairs(n: Int): Int {
    val a = ((1 + sqrt(5.0)) / 2).pow(n + 1)
    val b = ((1 - sqrt(5.0)) / 2).pow(n + 1)
    return (1 / sqrt(5.0) * (a - b)).toInt()
}