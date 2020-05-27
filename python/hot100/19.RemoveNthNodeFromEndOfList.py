#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from hot100.ListNode import ListNode


class RemoveNthNodeFromEndOfList:
    # https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-by-l/
    # 双指针
    # Runtime: 24 ms, faster than 97.27% of Python3 online submissions for Remove Nth Node From End of List.
    # Memory Usage: 14 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        headNode = ListNode()
        headNode.next = head
        start = headNode
        end = headNode
        for i in range(n):
            end = end.next
        while end.next is not None:
            start = start.next
            end = end.next
        start.next = start.next.next
        return headNode.next


if __name__ == "__main__":
    check = RemoveNthNodeFromEndOfList()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    check.removeNthFromEnd(node1, 2).log()

    # node1.next = node2
    # check.removeNthFromEnd(node1, 2).log()
