#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

# https://leetcode.com/problems/add-two-numbers/
# 用两个链表存储了两个数   求两数之和的链表
from hot100.LIstNode import ListNode


class AddTwoNumbers:

    # divmode 函数
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """注意考虑特殊情况，题目并没有说是相同长度，只是非空而已"""
        res = tmp = ListNode(0)
        # 进位
        add = 0
        while l1 or l2 or add:
            sum_one_num = l1.val + add if l1 else add
            sum_one_num += l2.val if l2 else 0
            # 利用divmod得到两个数的整数商和余数
            add, sum_one_num = divmod(sum_one_num, 10)
            tmp.next = ListNode(sum_one_num)
            tmp = tmp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next

    # Runtime: 68 ms, faster than 84.69% of Python3 online submissions for Add Two Numbers.
    # Memory Usage: 14 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumNum = l1.val + l2.val
        extraAdd = sumNum // 10
        sumNum = sumNum % 10
        rs = ListNode(sumNum)
        tempNode = rs
        l1Temp = l1.next
        l2Temp = l2.next
        while True:
            if l1Temp is None and l2Temp is None and extraAdd is 0: break
            val1 = 0
            val2 = 0
            if l1Temp is not None:
                val1 = l1Temp.val
                l1Temp = l1Temp.next
            if l2Temp is not None:
                val2 = l2Temp.val
                l2Temp = l2Temp.next
            sumNum = val1 + val2 + extraAdd
            extraAdd = sumNum // 10
            sumNum = sumNum % 10
            temp1Node = ListNode(sumNum)
            tempNode.next, tempNode = temp1Node, temp1Node
        return rs


if __name__ == "__main__":
    node2 = ListNode(2)
    node4 = ListNode(4)
    node3 = ListNode(3)

    node5 = ListNode(5)
    node6 = ListNode(6)
    node42 = ListNode(4)

    node2.next = node4
    node4.next = node3

    node5.next = node6
    node6.next = node42

    check = AddTwoNumbers()
    rs = check.addTwoNumbers(node2, node5)
    tempNode = rs
    while True:
        if tempNode is None:
            break
        print(tempNode.val)
        tempNode = tempNode.next
