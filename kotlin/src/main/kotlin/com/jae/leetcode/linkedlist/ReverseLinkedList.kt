package com.jae.leetcode.linkedlist

/**
 * @Description 翻转一个单链表 https://leetcode.com/problems/reverse-linked-list/
 * @Author Jae
 * @Date 2019/2/12 09:47
 **/

fun main(args: Array<String>) {
    val listNode = ListNode.createNumListNode(6)
    reverseList(listNode)?.print()
}

private fun reverseList(head: ListNode?): ListNode? {
    //方法一两两翻转 156 ms
    //    var temp: ListNode? = head ?: return null
    //    var pre: ListNode? = null
    //    while (temp!= null) {
    //        val next = temp.next
    //        temp.next = pre
    //        pre = temp
    //        temp = next
    //    }
    //    return pre
    //方法二 递归将当前位置和下一个位置翻转  152 ms
    if (head?.next == null) return head
    val list = reverseList(head.next)
    head.next!!.next = head
    head.next = null
    return list
}