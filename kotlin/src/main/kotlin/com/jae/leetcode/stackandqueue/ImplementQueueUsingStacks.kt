package com.jae.leetcode.stackandqueue

import java.util.*

/**
 * @Description: https://leetcode.com/problems/implement-queue-using-stacks/description/   232. Implement Queue using Stacks
 * @Author yj
 * @Date 2019-04-16 09:52
 **/

fun main(args: Array<String>) {
    val obj = MyQueue()
    obj.push(1)
    println(obj.peek())
    println(obj.pop())
    println(obj.empty())
}

//入队列的时候全放到 输入栈中，出队列时候全放到 出栈为空就将所有入栈元素放到出栈中 输出栈出值
private class MyQueue() {//180 ms
    //输入stack
    val inStack: Stack<Int> = Stack()

    //输出stack
    val outStack: Stack<Int> = Stack()

    fun push(x: Int) = inStack.push(x)

    fun pop(): Int {
        if (outStack.isEmpty()) {
            while (!inStack.empty()) {
                outStack.push(inStack.pop())
            }
        }
        return outStack.pop()
    }

    fun peek(): Int {
        if (outStack.isEmpty()) {
            while (!inStack.empty()) {
                outStack.push(inStack.pop())
            }
        }
        return outStack.peek()
    }

    fun empty() = outStack.empty() && inStack.empty()

}
