#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from typing import List

from hot100.ListNode import ListNode


# https://leetcode.com/problems/merge-k-sorted-lists/
class MergeKSortedLists:

    # 1.优先队列
    # 依次加入优先级队列，每次都取出最小的
    # heapq
    # Runtime: 108 ms, faster than 70.85% of Python3 online submissions for Merge k Sorted Lists.
    # Memory Usage: 17.6 MB, less than 12.12% of Python3 online submissions for Merge k Sorted Lists.
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None: return None
        import heapq
        head = []
        headNode = ListNode()
        tempNode = ListNode()
        headNode.next = tempNode
        for i in range(len(lists)):
            if lists[i] is None: continue
            heapq.heappush(head, (lists[i].val, i))
        if head is None: return None
        while head:
            val, index = heapq.heappop(head)
            tempNode.next = ListNode(val)
            tempNode = tempNode.next
            if lists[index]:
                lists[index] = lists[index].next
                if lists[index] is not None:
                    heapq.heappush(head, (lists[index].val, index))
        return headNode.next.next

    # 2.分治，两个两个处理
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        length = len(lists)
        return self.merge(lists, 0, length - 1)

    def merge(self, lists, left, right):
        if right == left:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # 3.对值平铺，排序
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        list1 = []
        for i in lists:
            while i:
                list1.append(i.val)
                i = i.next
        list1.sort()
        prev = ListNode()
        res = prev
        for i in list1:
            node = ListNode(i)
            prev.next = node
            prev = node
        return res.next


if __name__ == "__main__":
    listNode1 = ListNode(1)
    listNode4 = ListNode(4)
    listNode5 = ListNode(5)
    listNode1.next = listNode4
    listNode4.next = listNode5

    listNode12 = ListNode(1)
    listNode3 = ListNode(3)
    listNode42 = ListNode(4)
    listNode12.next = listNode3
    listNode3.next = listNode42

    listNode2 = ListNode(2)
    listNode6 = ListNode(6)
    listNode2.next = listNode6

    check = MergeKSortedLists()
    check.mergeKLists2([listNode1, listNode12, listNode2]).log()
