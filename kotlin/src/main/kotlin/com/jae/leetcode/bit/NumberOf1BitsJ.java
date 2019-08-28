package com.jae.leetcode.bit;

/**
 * @Description: https://leetcode.com/problems/number-of-1-bits/
 * @Author Jae
 * @Date 2019-08-28 09:36
 **/
class NumberOf1BitsJ {
    public static void main(String[] args) {
        System.out.println(hammingWeight(0b00000000000000000000000000001011));
        System.out.println(hammingWeight(0b00000000000000000000000010000000));
        System.out.println(hammingWeight(0b11111111111111111111111111111101));
    }

    //Runtime: 0 ms, faster than 100.00% of Java online submissions for Number of 1 Bits.
    //Memory Usage: 33.6 MB, less than 5.41% of Java online submissions for Number of 1 Bits.
    private static int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count++;
            n = n & (n - 1);
        }
        return count;
    }
}

