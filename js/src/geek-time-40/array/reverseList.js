/*

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

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
var reverseList = function (head, prev) {
    if (head) {
        var tmp = head.next
        head.next = prev
        prev = head
        head = tmp
        return reverseList(head, prev)
    } else {
        return prev
    }
};


// 迭代法   O(n)
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



// 单向链表节点
function ListNode(val) {
    this.val = val;
    this.next = null;
}