package com.jae.leetcode

/**
 * @Description
 * @Author Jae
 * @Date 2019/2/11 18:26
 **/

fun main(args: Array<String>) {
    // 递归k个反转
    // 反转方式是  head next curr 移动
    // curr默认是尾部指向的下一个不停的向前移动
    // next向head移动
    // head移动到curr前面
    val listNode1 = ListNode(1)
    val listNode2 = ListNode(2)
    val listNode3 = ListNode(3)
    val listNode4 = ListNode(4)
    listNode1.next = listNode2
    listNode2.next = listNode3
    listNode3.next = listNode4
    val swapPairs = reverseKGroup(listNode1, 4)
    var show = swapPairs
    while (show != null) {
        println(show.`val`)
        show = show.next
    }
}

private fun reverseKGroup(head: ListNode?, k: Int): ListNode? {
    var headNode: ListNode? = head ?: return null
    var count = 0
    var curr: ListNode? = headNode
    while (curr != null && count != k) {
        curr = curr.next
        count++
    }

    if (count == k) {
        curr = reverseKGroup(curr, k)
        while (count-- > 0) {
            val temp = headNode!!.next
            headNode.next = curr  //头放到尾部
            curr = headNode  //尾部位置向前移
            headNode = temp //第二位置移到头部
        }
        headNode = curr
    }
    return headNode
}
