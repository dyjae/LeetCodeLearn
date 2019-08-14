package com.jae.leetcode.recursive

/**
 * @Description: https://leetcode.com/problems/generate-parentheses/
 * @Author yj
 * @Date 2019-08-14 18:20
 **/
fun main(args: Array<String>) {
    generateParenthesis(2).forEach(::println)
}

//Runtime: 192 ms, faster than 26.83% of Kotlin online submissions for Generate Parentheses.
//Memory Usage: 35.5 MB, less than 100.00% of Kotlin online submissions for Generate Parentheses.
fun generateParenthesis(n: Int): List<String> {
    val rs = emptyList<String>().toMutableList()
    gen(rs, n, n, "")
    return rs
}

fun gen(rs: MutableList<String>, left: Int, right: Int, rsStr: String) {
    if (left == 0 && right == 0) {
        rs.add(rsStr)
        return
    }
    if (left > 0) gen(rs, left - 1, right, "$rsStr(")
    if (right > left) gen(rs, left, right - 1, "$rsStr)")
}