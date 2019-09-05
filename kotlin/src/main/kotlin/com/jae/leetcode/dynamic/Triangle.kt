package com.jae.leetcode.dynamic

import kotlin.math.min

/**
 * @Description:
 * @Author Jae
 * @Date 2019-09-05 18:49
 **/

fun main(args: Array<String>) {
    val input = listOf(
        listOf(2),
        listOf(3, 4),
        listOf(6, 5, 7),
        listOf(4, 1, 8, 3)
    )
    println(minimumTotal(input))
}

//Runtime: 156 ms, faster than 95.83% of Kotlin online submissions for Triangle.
//Memory Usage: 36.4 MB, less than 100.00% of Kotlin online submissions for Triangle.
//fun minimumTotal(triangle: List<List<Int>>): Int {
//    val rs = triangle[triangle.size - 1].toIntArray()
//    for (i in triangle.size - 2 downTo 0) {//从倒数第一层数到第0层
//        for (j in 0 until triangle[i].size) {
//            rs[j] = triangle[i][j] + min(rs[j], rs[j + 1])
//        }
//    }
//    return rs[0]
//}

//152
fun minimumTotal(triangle: List<List<Int>>): Int {
    val n = triangle.size
    val arr = Array(2) { IntArray(n + 1) { Int.MAX_VALUE}}
    arr[0][0] = 0
    var p = 0
    for(i in 0 until n){
        arr[p xor 1] = IntArray(n + 1) { Int.MAX_VALUE}
        for(j in 0 until triangle[i].size){
            arr[p xor 1][j] = minOf(arr[p xor 1][j], arr[p][j] + triangle[i][j])
            arr[p xor 1][j + 1] = minOf(arr[p xor 1][j + 1], arr[p][j] + triangle[i][j])
        }
        p = p xor 1
    }
    var res = Int.MAX_VALUE
    for(v in arr[p]) res = minOf(res, v)
    return res
}