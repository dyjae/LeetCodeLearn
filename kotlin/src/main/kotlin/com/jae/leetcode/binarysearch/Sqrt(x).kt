package com.jae.leetcode.binarysearch

fun main(args: Array<String>) {
    println(mySqrt(8))
}

//Runtime: 128 ms, faster than 96.10% of Kotlin online submissions for Sqrt(x).
//Memory Usage: 31.5 MB, less than 100.00% of Kotlin online submissions for Sqrt(x).
fun mySqrt(x: Int): Int {
    if (x == 0 || x == 1) return x
    var start = 1
    var end = x
    var mid = 0

    while (start <= end) {
        val zj = start + (end - start) / 2
        when {
            x / zj == zj -> return zj
            x / zj < zj -> {
                end = zj - 1

            }
            x / zj > zj -> {
                start = zj + 1
                mid = zj
            }
        }
    }
    return mid
}

//116
//fun mySqrt(x: Int): Int {
//    if(x == 0) return 0
//    var start = 1
//    var end = Int.MAX_VALUE
//
//    while (true) {
//        val mid = start + (end - start)/2
//        if (mid > x/mid) {
//            end = mid - 1
//        } else {
//            if ((mid + 1) > x/(mid + 1)) return mid
//            start = mid + 1
//        }
//    }
//}