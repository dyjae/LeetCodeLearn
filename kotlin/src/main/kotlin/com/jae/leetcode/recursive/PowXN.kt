package com.jae.leetcode.recursive

/**
 * @Description:https://leetcode.com/problems/powx-n/
 * @Author yj
 * @Date 2019-08-10 18:12
 **/

fun main(args: Array<String>) {
    println(myPow(2.0, 2))
}

//使用非递归的方式
//Runtime: 172 ms, faster than 22.41% of Kotlin online submissions for Pow(x, n).
//Memory Usage: 31.8 MB, less than 100.00% of Kotlin online submissions for Pow(x, n).
fun myPow(x: Double, n: Int): Double {
    if (x == 1.0) return x
    if (n == 0) return 1.0
    return when (n) {
        Int.MAX_VALUE ->
            when {
                x < 0 -> -1.0
                else -> 0.0
            }
        Int.MIN_VALUE ->
            when {
                x < 0 -> 1.0
                else -> 0.0
            }
        else -> {
            var param = x
            var loop = n
            if (loop < 0) {
                param = 1 / x
                loop = -loop
            }
            var rs = 1.0
            while (loop != 0) {
                if (loop.and(1) > 0) {
                    rs *= param
                }
                param *= param
                loop = loop.shr(1)
            }
            return rs
        }
    }
}

//时间复杂度 O(logn)
//Runtime: 140 ms, faster than 93.10% of Kotlin online submissions for Pow(x, n).
//Memory Usage: 31.3 MB, less than 100.00% of Kotlin online submissions for Pow(x, n).
//fun myPow(x: Double, n: Int): Double {
//    if (x == 1.0) return x
//    if (n == 0) return 1.0
//    return when {
//        n == Int.MAX_VALUE ->
//            when {
//                x < 0 -> -1.0
//                else -> 0.0
//            }
//        n == Int.MIN_VALUE ->
//            when {
//                x < 0 -> 1.0
//                else -> 0.0
//            }
//        n < 0 -> 1 / myPow(x, -n)
//        n % 2 > 0 -> x * myPow(x, n - 1) // n奇数时
//        else -> myPow(x * x, n / 2)
//    }
//}


//Runtime: 160 ms, faster than 36.21% of Kotlin online submissions for Pow(x, n).
//Memory Usage: 33.2 MB, less than 100.00% of Kotlin online submissions for Pow(x, n).
//fun myPow(x: Double, n: Int): Double {
//    if (x == 1.0) return x
//    return when {
//        n == Int.MAX_VALUE ->
//            when {
//                x > 0 -> 0.0
//                x < 0 -> -1.0
//                else -> 0.0
//            }
//        n == Int.MIN_VALUE ->
//            when {
//                x > 0 -> 0.0
//                x < 0 -> 1.0
//                else -> 0.0
//            }
//        n > 0 -> pow(x, 1.0, n)
//        n < 0 -> 1 / pow(x, 1.0, Math.abs(n))
//        else -> 1.0
//    }
//}
//
//tailrec fun pow(x: Double, y: Double, n: Int): Double {
//    if (n == 0) return y
//    val z = y * x
//    return pow(x, z, n - 1)
//}

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