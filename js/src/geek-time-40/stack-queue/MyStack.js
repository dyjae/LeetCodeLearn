/*

使用队列实现栈的下列操作：
    push(x) -- 元素 x 入栈
    pop() -- 移除栈顶元素
    top() -- 获取栈顶元素
    empty() -- 返回栈是否为空

注意:
你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

0. 使用数组模拟Queue
方法与用堆栈实现队列类似
1. 定义两个队列 Queue
    一个输入队列，push只添加到输入队列
    一个输出队列，pop/peek时，若输出队列为空，将输入队列全部推入到输出队列


*/

/**
 * Initialize your data structure here.
 */
var MyStack = function() {
    
};

/**
 * Push element x onto stack. 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    
};

/**
 * Removes the element on top of the stack and returns that element.
 * @return {number}
 */
MyStack.prototype.pop = function() {
    
};

/**
 * Get the top element.
 * @return {number}
 */
MyStack.prototype.top = function() {
    
};

/**
 * Returns whether the stack is empty.
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */