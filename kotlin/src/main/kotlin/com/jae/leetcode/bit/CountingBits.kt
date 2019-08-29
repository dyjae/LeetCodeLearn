package com.jae.leetcode.bit

/**
 * @Description:https://leetcode.com/problems/counting-bits/description/
 * @Author Jae
 * @Date 2019-08-29 10:05
 **/

fun main(args: Array<String>) {
    countBits(2).forEach(::print)
    println()
    countBits(5).forEach(::print)
}


//rs[0] =0
//rs[1]     0001 0000
//rs[2]     0010 0001
//rs[3]     0011 0010
//Runtime: 176 ms, faster than 68.00% of Kotlin online submissions for Counting Bits.
//Memory Usage: 38.1 MB, less than 100.00% of Kotlin online submissions for Counting Bits.
fun countBits(num: Int): IntArray {
    val rs = IntArray(num + 1)
    for (i in 1..num)
        rs[i] = rs[i.and(i - 1)] + 1
    return rs
}

//156
//fun countBits(num: Int): IntArray {
//    var memo = IntArray(num+1)
//    memo[0] = 0
//
//    var gap = 1
//    for(i in 1..num) {
//        if(i == gap * 2) {
//            gap *= 2
//        }
//        memo[i] = memo[i-gap] + 1
//    }
//    return memo
//}