package com.jae.leetcode

/**
 * @Description
 * @Author Jae
 * @Date 2019/2/3 14:53
 **/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null

    override fun toString(): String = `val`.toString()

    //打印ListNode
    fun print() {
        var show: ListNode? = this
        while (show != null) {
            println(show.`val`)
            show = show.next
        }
    }

    companion object {
        /**
         * @Description: 创建长度为num的链表，开始的数值为startNum
         * @author: Jae
         * @date: 2019/2/12 10:09
         */
        fun createNumListNode(num: Int, startNum: Int = 1): ListNode {
//            println("num=$num,startNum=$startNum")
            val listNode = ListNode(startNum)
            if (num > 1) {
                val nextListNode = createNumListNode(num - 1, startNum + 1)
                listNode.next = nextListNode
            }
            return listNode
        }
    }
}