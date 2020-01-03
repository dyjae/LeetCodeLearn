/*

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    var none = {}
    none.next = head

    var pre = none
    var end = none

    while (end.next != null) {
        for (var i = 0; i < k && end != null; i++) end = end.next;
        if (end == null) break;
        var start = pre.next;
        var next = end.next;
        end.next = null;
        pre.next = reverseList(start);
        start.next = next;
        pre = start;

        end = pre;
    }
    return none.next;

};

var reverseList = function (head) {
    var cur = head
    var prev = null
    while (cur) {
        var tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    }
    return prev
};



function ListNode(val) {
    this.val = val
    this.next = null
}

var i1 = new ListNode(1)
var i2 = new ListNode(2)
var i3 = new ListNode(3)
var i4 = new ListNode(4)
var i5 = new ListNode(5)

i4.next = i5
i3.next = i4
i2.next = i3
i1.next = i2

console.log(reverseKGroup(i1, 2))