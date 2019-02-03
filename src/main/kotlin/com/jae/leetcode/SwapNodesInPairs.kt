package com.jae.leetcode

/**
 * @Description
 * @Author Jae
 * @Date 2019/2/3 14:52
 **/

fun main(args: Array<String>) {
    val listNode1 = ListNode(1)
    val listNode2 = ListNode(2)
    val listNode3 = ListNode(3)
    val listNode4 = ListNode(4)
    listNode1.next = listNode2
    listNode2.next = listNode3
    listNode3.next = listNode4
    val swapPairs = swapPairs(listNode1)
    var show = swapPairs
    while (show != null) {
        println(show.`val`)
        show = show.next
    }
}

private fun swapPairs(head: ListNode?): ListNode? {
    //172ms
    head ?: return null
    //先定义一个头结点
    val result = ListNode(0)
    result.next = head
    var pre = result
    while (pre.next != null && pre.next!!.next != null) {
        val temp1 = pre.next!!
        val temp2 = temp1.next!!
        val next = temp2.next
        //两两交换位置
        temp2.next = temp1
        temp1.next = next
        pre.next = temp2
        pre = temp1
    }
    return result.next
    //192ms
    //https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11022/Kotlin
//    val seq = generateSequence(head) { it.next }
//    fun swapNode(node1: ListNode, node2: ListNode) {
//        val temp = node1.`val`
//        node1.`val` = node2.`val`
//        node2.`val` = temp
//    }
//
//    seq.fold<ListNode, ListNode?>(null) { acc, listNode ->
//                  acc?.also { swapNode(acc, listNode) };
//                  if (acc == null) listNode else null
//              }
//    return head
}