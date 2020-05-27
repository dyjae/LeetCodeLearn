#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

# https://leetcode.com/problems/merge-two-sorted-lists/
from hot100.ListNode import ListNode


class MergeTwoSortedLists:

    # 递归
    # Runtime: 32 ms, faster than 90.02% of Python3 online submissions for Merge Two Sorted Lists.
    # Memory Usage: 14 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
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

    # Runtime: 40 ms, faster than 44.62% of Python3 online submissions for Merge Two Sorted Lists.
    # Memory Usage: 13.8 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.headNode = ListNode()
        self.tmpNode = None
        if l1 is None and l2.next is None:
            return None
        l1Head = l1
        l2Head = l2
        while True:
            if l1Head is None and l2Head is not None:
                self.__parse_list(l2Head)
                break
            elif l2Head is None and l1Head is not None:
                self.__parse_list(l1Head)
                break
            l1val = l1Head.val
            l2val = l2Head.val
            if l1val >= l2val:
                self.__parse_list_val(l2val)
                l2Head = l2Head.next
            else:
                self.__parse_list_val(l1val)
                l1Head = l1Head.next
        return self.headNode.next

    def __parse_list_val(self, val):
        if self.tmpNode is None:
            node = ListNode(val)
            self.headNode.next = node
            self.tmpNode = node
        else:
            self.tmpNode.next = ListNode(val)
            self.tmpNode = self.tmpNode.next

    def __parse_list(self, in_list):
        if self.tmpNode is None:
            self.headNode.next = in_list
        else:
            self.tmpNode.next = in_list


if __name__ == "__main__":
    list1 = ListNode(1)
    list2 = ListNode(2)
    list4 = ListNode(4)

    list1.next = list2
    list2.next = list4

    list12 = ListNode(1)
    list3 = ListNode(3)
    list42 = ListNode(4)

    list12.next = list3
    list3.next = list42

    check = MergeTwoSortedLists()
    check.mergeTwoLists(list1, list12).log()

    # list0 = ListNode(0)
    # check.mergeTwoLists(None, list0).log()
