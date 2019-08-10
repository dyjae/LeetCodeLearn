package com.jae.leetcode.recursive

/**
 * @Description:https://leetcode.com/problems/powx-n/
 * @Author yj
 * @Date 2019-08-10 18:12
 **/

fun main(args: Array<String>) {
    println(myPow(2.1, 3))
}

//Runtime: 160 ms, faster than 36.21% of Kotlin online submissions for Pow(x, n).
//Memory Usage: 33.2 MB, less than 100.00% of Kotlin online submissions for Pow(x, n).
fun myPow(x: Double, n: Int): Double {
    if (x == 1.0) return x
    return when {
        n == Int.MAX_VALUE ->
            when {
                x > 0 -> 0.0
                x < 0 -> -1.0
                else -> 0.0
            }
        n == Int.MIN_VALUE ->
            when {
                x > 0 -> 0.0
                x < 0 -> 1.0
                else -> 0.0
            }
        n > 0 -> pow(x, 1.0, n)
        n < 0 -> 1 / pow(x, 1.0, Math.abs(n))
        else -> 1.0
    }
}

tailrec fun pow(x: Double, y: Double, n: Int): Double {
    if (n == 0) return y
    val z = y * x
    return pow(x, z, n - 1)
}

//136
//fun myPow(x: Double, n: Int): Double {
//    if (n >= 0) return pow(x, n)
//    var c = n
//    var x2 = x
//    if (n == Int.MIN_VALUE) {
//        c = n / 2
//        x2 = x * x
//    }
//    return 1 / pow(x2, -c)
//}
//
//fun pow(x: Double, n: Int): Double {
//    if (n == 0) return 1.0
//    if (n == 1) return x
//    val r = pow(x, n / 2)
//    return r * r * pow(x, n % 2)
//}

//124
//    fun myPow(x: Double, n: Int): Double {
//        if (n == 0)   return 1.0
//        if (n == 1)   return x
//        if (x == -1.0)  return if (n % 2 == 0) 1.0 else -1.0
//        if (x == 1.0) return 1.0
//        if (x == 0.0)  return 0.0
//        if (n < -1000) return 0.0
//
//        if (n < 0)  return 1 / myPow(x, -n)
//
//        if ((n % 2) == 0)
//        {
//            return myPow(x * x, n / 2)
//        }
//        else
//        {
//            return x * myPow(x * x, n / 2)
//        }
//    }