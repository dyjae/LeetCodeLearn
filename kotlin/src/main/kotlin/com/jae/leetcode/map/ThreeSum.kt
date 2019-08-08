package com.jae.leetcode.map

/**
 * @Description: https://leetcode.com/problems/3sum/
 * @Author yj
 * @Date 2019-07-25 10:19
 **/

fun main(args: Array<String>) {
//    Given array nums = [-1, 0, 1, 2, -1, -4],
//
//    A solution set is:
//    [
//        [-1, 0, 1],
//        [-1, -1, 2]
//    ]

    //-4 -1 -1 0 1 2
    val array = intArrayOf(-1, 0, 1, 2, -1, -4)
    threeSum(array).forEach {
        it.forEach { nums -> print(nums) }
        println()
    }

}

//Runtime: 364 ms, faster than 96.05% of Kotlin online submissions for 3Sum.
//Memory Usage: 45.5 MB, less than 100.00% of Kotlin online submissions for 3Sum.
fun threeSum(nums: IntArray): List<List<Int>> {
    nums.sort()
    val rs = ArrayList<ArrayList<Int>>()
    //用来去重
    nums.forEachIndexed { index, value ->
        if (index != 0 && value == nums[index - 1]) return@forEachIndexed
        var lIndex = index + 1
        var rIndex = nums.size - 1
        while (lIndex < rIndex) {
            val total = value + nums[lIndex] + nums[rIndex]
            when {
                total == 0 -> {
                    rs.add(arrayListOf(value, nums[lIndex], nums[rIndex]))
                    //用来去重
                    while (nums.size-1 > lIndex && nums[lIndex] == nums[++lIndex]) {
                    }
                    while (rIndex > 0 && nums[rIndex] == nums[--rIndex]) {
                    }
                }
                total < 0 -> lIndex++
                total > 0 -> rIndex--
            }
        }

    }
    return rs
}

// 352ms
fun threeSum2(nums: IntArray): List<List<Int>> {
    val ans: MutableList<List<Int>> = mutableListOf()
    if (nums.size < 3) return ans
    nums.sort()
    for (i in nums.indices) {
        if (i != 0 && nums[i] == nums[i - 1]) continue
        var j = i + 1
        var k = nums.size - 1
        while (j < k) {
            when {
                nums[j] + nums[k] + nums[i] == 0 -> {
                    ans.add(listOf(nums[i], nums[j++], nums[k--]))
                    while (j < k && nums[j] == nums[j - 1]) j++
                    while (j < k && nums[k] == nums[k + 1]) k--
                }
                nums[j] + nums[k] + nums[i] > 0 -> k--
                else -> j++
            }
        }
    }
    return ans.toList()
}