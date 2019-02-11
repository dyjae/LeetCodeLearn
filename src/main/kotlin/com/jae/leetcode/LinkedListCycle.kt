package com.jae.leetcode

/**
 * @Description
 * @Author Jae
 * @Date 2019/2/3 16:12
 **/
//Given a linked list, determine if it has a cycle in it.
//
//To represent a cycle in the given linked list,
// we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
// If pos is -1, then there is no cycle in the linked list.
//判断是否有环
fun main(args: Array<String>) {
    //三种方式
    //1 硬破解 读到最后一个指针指向空就没有环 (限定多少秒内)
    //2 用Set存已经遍历过得 O（n）
    //3 用快慢指针，慢指针每次移动一步，快指针每次移动两步，当指针相遇就是有环，快指针走到头就是没有环 O(n)
    val listNode1 = ListNode(1)
    val listNode2 = ListNode(2)
    val listNode3 = ListNode(3)
    val listNode4 = ListNode(4)
    listNode1.next = listNode2
    listNode2.next = listNode3
    listNode3.next = listNode4
    listNode4.next = listNode2
    println(hasCycle(listNode1))
}

private fun hasCycle(head: ListNode): Boolean {
    var lowPointer: ListNode? = head
    var fastPoint: ListNode? = head
    while (fastPoint != null && lowPointer != null && fastPoint.next != null) {
        lowPointer = lowPointer.next!!
        fastPoint = fastPoint.next!!.next!!
        if (lowPointer == fastPoint) return true
    }
    return false
}


