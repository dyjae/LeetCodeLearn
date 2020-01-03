/*

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。


进阶：
你是否可以不用额外空间解决此题？

思路同 ./hasCycle.js

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
// Set法
var detectCycle = function(head) {
    if (!head || !head.next) return null
    var set = new Set()
    while (head) {
        if(set.has(head)) {
            return head
        }
        set.add(head)
        head = head.next
    }
    return null
};


function ListNode(val) {
    this.val = val
    this.next = null
}