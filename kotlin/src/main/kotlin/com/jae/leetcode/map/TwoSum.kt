package com.jae.leetcode.map

import java.util.HashMap

/**
 * @Description:    1. Two Sum
 *                  https://leetcode.com/problems/two-sum/
 * @Author yj
 * @Date 2019-07-23 09:17
 **/

fun main(args: Array<String>) {
    val nums = arrayOf(3, 3).toIntArray()
    val rs = twoSum(nums, 6)
    if (rs.isEmpty()) {
        println("没有")
    } else {
        rs.forEach(::println)
    }
}

//Runtime: 172 ms, faster than 98.34% of Kotlin online submissions for Two Sum.
//Memory Usage: 36.9 MB, less than 100.00% of Kotlin online submissions for Two Sum.
fun twoSum(nums: IntArray, target: Int): IntArray {
    //value(差) -> index
    val map = HashMap<Int, Int>()
    nums.forEachIndexed { index, value ->
        if (map.keys.contains(value)) {
            map[value]?.let {
                return intArrayOf(it, index)
            } ?: return@forEachIndexed
        } else {
            map[target - value] = index
        }
    }
    return emptyArray<Int>().toIntArray()
}

//fastSolution
fun twoSum2(nums: IntArray, target: Int): IntArray {
    val map: HashMap<Int, Int> = HashMap<Int, Int>()
    var en: Int = -1
    var st: Int = -1
    for (index in nums.indices) {
        val diff = target - nums[index]
        if (map.containsKey(diff)) {
            st = map[diff]!!
            en = index
        }
        map[nums[index]] = index
    }
    return intArrayOf(st, en)
}

//用Set碰到  3，3  6 这种情况就有问题了
//fun twoSum(nums: IntArray, target: Int): IntArray {
//    val numsSet = nums.toMutableSet()
//    nums.forEachIndexed { index, value ->
//        numsSet.remove(value)
//        if (numsSet.contains(target - value)) {
//            val index2 = nums.indexOf(target - value)
//            return arrayOf(index, index2).toIntArray()
//        }
//    }
//    return emptyArray<Int>().toIntArray()
//}

