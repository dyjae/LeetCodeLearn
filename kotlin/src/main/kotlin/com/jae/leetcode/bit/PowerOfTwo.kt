package com.jae.leetcode.bit

/**
 * @Description: https://leetcode.com/problems/power-of-two/
 * @Author Jae
 * @Date 2019-08-29 09:37
 **/

fun main(args: Array<String>) {
    println(isPowerOfTwo(1))
    println(isPowerOfTwo(16))
    println(isPowerOfTwo(218))
}

//Runtime: 116 ms, faster than 100.00% of Kotlin online submissions for Power of Two.
//Memory Usage: 31.5 MB, less than 100.00% of Kotlin online submissions for Power of Two.
fun isPowerOfTwo(n: Int): Boolean {
    return n != 0 && (n.and(n - 1) == 0)
}