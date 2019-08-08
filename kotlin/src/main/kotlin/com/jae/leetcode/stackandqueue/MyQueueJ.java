package com.jae.leetcode.stackandqueue;

import java.util.Stack;

/**
 * @Description:
 * @Author yj
 * @Date 2019-04-16 10:18
 **/
class MyQueueJ {//Runtime: 54 ms

    private Stack<Integer> inStack = new Stack<Integer>();

    private Stack<Integer> outStack = new Stack<Integer>();

    /**
     * Push element x onto stack.
     */
    public void push(int x) {
        inStack.push(x);
    }

    /**
     * Removes the element on top of the stack and returns that element.
     */
    public int pop() {
        move();
        return outStack.pop();
    }

    /**
     * Get the top element.
     */
    public int peek() {
        move();
        return outStack.peek();
    }

    private void move() {
        if (outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                outStack.push(inStack.pop());
            }
        }
    }

    /**
     * Returns whether the stack is empty.
     */
    public boolean empty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }

}