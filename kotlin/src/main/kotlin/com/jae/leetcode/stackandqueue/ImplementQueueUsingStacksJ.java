package com.jae.leetcode.stackandqueue;

import java.util.*;

/**
 * @Description: https://leetcode.com/problems/implement-queue-using-stacks/description/   232. Implement Queue using Stacks
 * @Author yj
 * @Date 2019-04-16 09:52
 **/

class ImplementQueueUsingStacksJ {//Runtime: 60 ms

    public static void main(String[] args) {
        MyQueueJ myQueue = new MyQueueJ();
        myQueue.push(1);
        myQueue.push(2);
        System.out.println("" + myQueue.peek());
        System.out.println("" + myQueue.pop());
        System.out.println("" + myQueue.empty());
    }

}

