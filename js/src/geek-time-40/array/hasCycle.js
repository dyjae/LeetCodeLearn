/*

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 

进阶：
你能用 O(1)（即，常量）内存解决此问题吗？


暴力迭代    O(n)
    判断next是否为null，执行一段时间，若无null，则存在环

Set     O(n)
    将next的指针地址存入Set，若发现相同地址，则存在环

快慢指针    O(2n)
    设置快慢指针，若发现指针指向重合，则存在环


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
 * @return {boolean}
 */
// 快慢指针法
var hasCycle = function(head) {
    var fast = head
    var slow = head
    while (fast && fast.next && fast.next.next) {
        fast = fast.next.next
        slow = slow.next
        if (fast === slow) {
            return true
        }
    }
    return false
};

function ListNode(val) {
    this.val = val
    this.next = null
}

var i1 = new ListNode(3)
// var i2 = new ListNode(2)
// var i3 = new ListNode(0)
// var i4 = new ListNode(-4)

// i4.next = i2
// i3.next = i4
// i2.next = i3
// i1.next = i2

console.log(hasCycle(i1))