package com.jae.leetcode.dequeue

import java.util.*

/**
 * @Description https://leetcode.com/problems/sliding-window-maximum/
 *          Runtime: 300 ms, faster than 46.67% of Kotlin online submissions for Sliding Window Maximum.
 * @Author yj
 * @Date 2019-07-16 08:33
 **/
fun main(args: Array<String>) {

    val nums = arrayOf(1, 3, -1, -3, 5, 3, 6, 7)
    val k = 3
    val rs = maxSlidingWindow(nums.toIntArray(), k)
    rs.forEach(System.out::println)


//    val deque = ArrayDeque<Int>(3)
//    deque.push(1)
//    deque.push(2)
//    deque.push(3)
//    deque.push(4)
//    println(deque.peek())
//    println(deque.peek())
//    println("deque中加入了1，2，3")
//    deque.addAll(arrayOf(1, 2, 3))
//    println("deque first is")
//    println(deque.first)
//    println("-----------------")
//    println("deque last is")
//    println(deque.last)
//    println("-----------------")
//    println("deque peek is")
//    println(deque.peek())
//    deque.push(4)
//    println(deque.peek())
//    println(deque.poll())
//    println(deque.peek())
//    println(deque.remove())
//    println(deque.peek())
//    deque.add(5)
//    println(deque.peek())

    //deque add是从尾部加   push从头部加  poll从头部取 remove从头部取  peek取头部

}


//1. maxHeap  维护堆(移除最早进入)  结果为最大值   NlogK
//2. Queue 左侧永远是最大的下标，先判断左侧是否滑出窗口，再从右侧开始移除比当前进入值小的，这时最左侧一定最大。
//Queue deque   双端进出   前进后出
private fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
    if (nums.isEmpty()) return IntArray(0)
    val rs = IntArray(nums.size - k + 1)
    val deque = ArrayDeque<Int>(k)
    nums.forEachIndexed { index, value ->
        //窗口已经滑到k个后，判断头部的index是否已经滑出
        if (index >= k && index - k + 1 > deque.peek()) deque.remove()
        //从尾部开始移除小的值
        while (deque.isNotEmpty() && nums[deque.peekLast()] < value) deque.removeLast()
        //从尾部加入index,这时头部肯定是最大的
        deque.add(index)
        //窗口输出值
        if (index - k + 1 >= 0) rs[index - k + 1] = nums[deque.peek()]
    }
    return rs
}


//244ms
//不停移动窗口比较值，最坏情况是k2复杂度，并没有上面方法好
fun maxSlidingWindow2(nums: IntArray, k: Int): IntArray {
    if (nums.isEmpty()) return IntArray(0) { 0 }
    var max = nums[0]
    var maxI = 0
    for (i in 1 until k) {
        if (nums[i] > max) {
            max = nums[i]
            maxI = i
        }
    }

    val res = IntArray(nums.size - k + 1) { max }

    for (i in k until nums.size) {
        if (nums[i] >= max) {
            max = nums[i]
            maxI = i
        } else if (nums[i - k] == max && maxI == i - k) {
            max = nums[i]
            maxI = i
            for (j in i - k + 1 until i) {
                if (nums[j] > max) {
                    max = nums[j]
                    maxI = j
                }
            }
        }
        res[i - k + 1] = max
    }

    return res
}