package com.jae.leetcode

/**
 * @Description 环形链表 https://leetcode.com/problems/linked-list-cycle-ii/
 * @Author Jae
 * @Date 2019/2/15 19:03
 **/

fun main(args: Array<String>) {
    val listNode1 = ListNode(1)
    val listNode2 = ListNode(2)
    val listNode3 = ListNode(3)
    val listNode4 = ListNode(4)
    listNode1.next = listNode2
    listNode2.next = listNode3
    listNode3.next = listNode4
    listNode4.next = listNode3
    println(detectCycle(listNode1))
}

private fun detectCycle(head: ListNode?): ListNode? {
    var slowPointer = head
    var quickPointer = head
    var hasCycle = false
    //快慢指针判断是否有环
    while (quickPointer?.next != null && quickPointer.next?.next != null) {
        slowPointer = slowPointer?.next
        quickPointer = quickPointer.next?.next
        if (slowPointer == quickPointer) {
            hasCycle = true
            break
        }
    }

    //有环就找环开始地方
    if (hasCycle) {
        var p = head
        while (p != slowPointer) {
            p = p?.next
            slowPointer = slowPointer?.next
        }
        return p
    }
    return null
}