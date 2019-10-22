package com.jae.leetcode.dynamic

/**
 * @Description:
 * @Author Jae
 * @Date 2019-10-22 09:18
 **/
object EditDistance {
    @JvmStatic
    fun main(args: Array<String>) {
        println(minDistance("horse", "ros"))
        println(minDistance("intention", "execution"))
    }

    //Runtime: 236 ms, faster than 25.00% of Kotlin online submissions for Edit Distance.
    //Memory Usage: 44.3 MB, less than 100.00% of Kotlin online submissions for Edit Distance.
    private fun minDistance(word1: String, word2: String): Int {
        val dp = Array(word1.length + 1) { Array(word2.length + 1) { 0 } }
        for (i in 0..word1.length) {
            dp[i][0] = i
        }
        for (j in 0..word2.length) {
            dp[0][j] = j
        }
        for (i in 1..word1.length) {
            for (j in 1..word2.length) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]
                } else {
                    dp[i][j] = minOf(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                }
            }
        }

        return dp[word1.length][word2.length]
    }
}