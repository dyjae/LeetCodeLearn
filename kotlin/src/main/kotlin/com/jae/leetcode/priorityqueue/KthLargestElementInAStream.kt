package com.jae.leetcode.priorityqueue

import java.util.*

/**
 * @Description 703. Kth Largest Element in a Stream
 *              https://leetcode.com/problems/kth-largest-element-in-a-stream/
 *              Runtime: 272 ms, faster than 90.00% of Kotlin online submissions for Kth Largest Element in a Stream.
 *              Memory Usage: 41.4 MB, less than 100.00% of Kotlin online submissions for Kth Largest Element in a Stream.
 * @Author yj
 * @Date
 **/

fun main(args: Array<String>) {
    val obj = KthLargest(3, intArrayOf(4,5,8,2))
    println(obj.add(3))
    println(obj.add(5))
    println(obj.add(10))
    println(obj.add(9))
    println(obj.add(4))
}

class KthLargest(private val k: Int, nums: IntArray) {

    var p = PriorityQueue<Int>(k)

    init {
        nums.forEach { add(it) }
    }

    fun add(value: Int): Int {
        if (p.size < k) {
           p.add(value)
        } else if (p.peek() < value) {
            p.poll()
            p.add(value)
        }
        return p.peek() ?: 0
    }

}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = KthLargest(k, nums)
 * var param_1 = obj.add(`val`)
 */