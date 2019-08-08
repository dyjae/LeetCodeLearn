package com.jae.leetcode.stackandqueue

import java.util.*

/**
 * @Description:https://leetcode.com/problems/implement-stack-using-queues/
 *                  find LinkedList have a function push it's add element to first
 *                  the LinkedList pop is push first
 *                  so use one LinkedList pop and push is the stack
 *                  top is first
 *
 *                  use add pop
 *                  Runtime: 172 ms, faster than 41.18% of Kotlin online submissions for Implement Stack using Queues.
 *                  Memory Usage: 33 MB, less than 100.00% of Kotlin online submissions for Implement Stack using Queues.
 *
 *                  use push pop
 *                  Runtime: 164 ms, faster than 47.06% of Kotlin online submissions for Implement Stack using Queues.
 *                  Memory Usage: 33.3 MB, less than 100.00% of Kotlin online submissions for Implement Stack using Queues.
 *
 *
 *
 * @Author yj
 * @Date 2019-04-18 18:27
 **/
object ImplementStackUsingQueues {
    @JvmStatic
    fun main(args: Array<String>) {
//        val l = LinkedList<Int>()
//        l.push(1)
//        l.push(2)
//        l.push(3)
//        l.isEmpty()
//        println(l.first)
//        println(l.pop())
//        println(l.pop())
//        println(l.pop())
        val stack = MyStack()
        println(stack.push(1))
        println(stack.push(2))
        println(stack.push(3))
        println(stack.top())
        println(stack.pop())
        println(stack.pop())
        println(stack.pop())
        println(stack.empty())


    }
}

private class MyStack() {
    val inQueue = LinkedList<Int>()

    val outQueue = LinkedList<Int>()

    var top = 0

    fun push(x: Int) {
        if (inQueue.isEmpty()) {
            outQueue.add(x)
        } else {
            inQueue.add(x)
        }
        top = x

    }

    fun pop() = when {
        outQueue.isNotEmpty() -> popQueue(outQueue, inQueue)
        inQueue.isNotEmpty() -> popQueue(inQueue, outQueue)
        else -> 0
    }

    private fun popQueue(outQueueP: LinkedList<Int>, inQueueP: LinkedList<Int>): Int {
        while (outQueueP.size > 2) {
            inQueueP.add(outQueueP.pop())
        }
        if (outQueueP.size == 2) {
            val temp = outQueueP.pop()
            top = temp
            inQueueP.add(temp)
        }
        return outQueueP.pop()
    }

    fun top(): Int {
        return top
    }

    fun empty(): Boolean {
        return outQueue.isEmpty() && inQueue.isEmpty()
    }
}