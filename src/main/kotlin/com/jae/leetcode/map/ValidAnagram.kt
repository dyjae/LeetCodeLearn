package com.jae.leetcode.map

/**
 * @Description:    https://leetcode.com/problems/valid-anagram/
 *
 *  两个map比较
 *  Runtime: 196 ms, faster than 67.42% of Kotlin online submissions for Valid Anagram.
 *  Memory Usage: 35.5 MB, less than 100.00% of Kotlin online submissions for Valid Anagram.
 *
 *  循环移除
 *  Runtime: 208 ms, faster than 49.44% of Kotlin online submissions for Valid Anagram.
 *  Memory Usage: 36.4 MB, less than 100.00% of Kotlin online submissions for Valid Anagram.
 *
 *  一个数组搞定，和a的值做比较，存入一个数组中，第二个就移除 156ms
 *  有一个问题是数组的大小，这里只针对字母
 *
 * @Author yj
 * @Date 2019-06-24 20:43
 **/
fun main(args: Array<String>) {
    val s = "afg"
    val t = "agf"
    println(isAnagram2(s, t))
}

fun isAnagram(s: String, t: String): Boolean {
    val sMap = HashMap<Char, Int>()
    val tMap = HashMap<Char, Int>()
    s.map { sMap[it] = sMap.getOrDefault(it, 0) + 1 }
    t.map { tMap[it] = tMap.getOrDefault(it, 0) + 1 }

//    t.forEach {
//        val i = sMap[it] ?: 0
//        when {
//            i < 1 -> return false
//            i == 1 -> sMap.remove(it)
//            else -> sMap[it] = sMap[it]?.minus(1) ?: 0
//        }
//
//    }

//    return sMap.isEmpty()
    return sMap == tMap
}

//156ms
fun isAnagram2(s: String, t: String): Boolean {
    val arr = IntArray(26) { 0 }
    s.forEach {
        arr[it - 'a']++
    }
    t.forEach {
        arr[it - 'a']--
    }
    return arr.firstOrNull { it != 0 } == null
}