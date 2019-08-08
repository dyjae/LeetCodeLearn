package com.jae.leetcode.stackandqueue

import java.util.*
import kotlin.collections.HashMap

/**
 * @Description: //https://leetcode.com/problems/valid-parentheses/description/  判断符号匹配
 * @Author yj
 * @Date 2019-04-12 09:42
 **/
fun main(args: Array<String>) {
    val s = "([)]"
    println(isValid(s))
}

private fun isValid(s: String): Boolean {
    val stack = Stack<Char>()
    val matchingMap = HashMap<Char, Char>() //右  左
    matchingMap[')'] = '('
    matchingMap[']'] = '['
    matchingMap['}'] = '{'
    s.toCharArray().forEach {
        if (matchingMap.values.contains(it)) {//左括号
            stack.push(it)//进左括号栈
        } else if (matchingMap.keys.contains(it)) {//右括号
            if (stack.isEmpty() || matchingMap[it] == stack.pop()) return false//左括号第一个出栈
        }
    }
    return stack.isEmpty()
}