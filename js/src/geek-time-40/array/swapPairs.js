/*

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

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
 * @return {ListNode}
 */
// 迭代法   O(n)
var swapPairs = function(head) {
    var pre = {}
    pre.next = head
    var res = head && (head.next || head) // 保存头结点
    while (pre.next && pre.next.next) {
        var a = pre.next
        var b = a.next
        var tmp = b.next
        pre.next = b
        b.next = a
        a.next = tmp
        pre = a
    }
    return res
};

function ListNode(val) {
    this.val = val
    this.next = null
}

var i1 = new ListNode(1)
var i2 = new ListNode(2)
var i3 = new ListNode(3)
var i4 = new ListNode(4)

i3.next = i4
i2.next = i3
i1.next = i2

console.log(swapPairs(i1))

console.log(swapPairs(new ListNode(1)))