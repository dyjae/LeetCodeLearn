package com.jae.leetcode.recursive

/**
 * @Description: https://leetcode.com/problems/majority-element/
 * @Author yj
 * @Date 2019-08-11 17:12
 **/

fun main(args: Array<String>) {
    println(majorityElement(intArrayOf(1, 2, 1, 2, 1, 2, 2)))
}

//TODO 分治做法


//Runtime: 208 ms, faster than 93.33% of Kotlin online submissions for Majority Element.
//Memory Usage: 41.9 MB, less than 100.00% of Kotlin online submissions for Majority Element.
fun majorityElement(nums: IntArray): Int {
    nums.sort()
    return nums[nums.size/2]
}


//196
//超过1/2 一定有相同或则最后一个
//fun majorityElement(nums: IntArray): Int {
//    var current = 0
//    var counter = 0
//    for (num in nums) {
//        if (counter == 0) {
//            current = num
//            counter = 1
//        } else {
//            if (current == num)
//                counter += 1
//            else
//                counter -= 1
//        }
//    }
//    return current
//}