package com.jae.leetcode.bit

/**
 * @Description: https://leetcode.com/problems/number-of-1-bits/
 * @Author Jae
 * @Date 2019-08-28 09:36
 **/

fun main(args: Array<String>) {
    println(hammingWeight(0b00000000000000000000000000001011))
    println(hammingWeight(0b00000000000000000000000010000000))
//    println(hammingWeight(0b11111111111111111111111111111101))
}

// you need to treat n as an unsigned value
fun hammingWeight(n: Int): Int {
    var temp = n
    var count = 0
    while (temp != 0) {
        count++
        temp = temp.and(temp - 1)
    }
    return count
}

//fun hammingWeight(n: Int): Int {
//    var temp = n
//    var count = 0
//    while (temp != 0) {
//        if (temp % 2 > 0) {
//            count++
//        }
//        temp = temp.shr(1)
//    }
//    return count
//}

