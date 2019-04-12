package com.jae.leetcode.stackandqueue;

import java.io.CharArrayWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/**
 * @Description:
 * @Author yj
 * @Date 2019-04-12 10:21
 **/
public class ValidParenthesesJ {
    public static void main(String[] args) {
        System.out.println(isValid("([])"));
    }

    private static boolean isValid(String s) {
        char[] chars = s.toCharArray();
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        for (char c : chars) {
            if (map.values().contains(c)) {//左括号
                stack.push(c);
            } else if (map.keySet().contains(c)) {//右括号
                if (stack.isEmpty() || stack.pop() != map.get(c)) return false;
            }
        }
        return stack.isEmpty();
    }
}
