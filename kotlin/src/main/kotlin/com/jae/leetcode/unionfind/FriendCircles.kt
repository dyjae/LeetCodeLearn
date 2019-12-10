package com.jae.leetcode.unionfind

/**
 * @Description: 547. Friend Circles   https://leetcode.com/problems/friend-circles/
 * @Author Jae
 * @Date 2019-12-09 09:21
 **/

object FriendCircles {
    @JvmStatic
    fun main(args: Array<String>) {
        println(
            findCircleNum(
                arrayOf(
                    intArrayOf(1, 0, 0, 1),
                    intArrayOf(0, 1, 1, 0),
                    intArrayOf(0, 1, 1, 1),
                    intArrayOf(1, 0, 1, 1)
                )
            )
        )
    }

//Runtime: 208 ms, faster than 53.85% of Kotlin online submissions for Friend Circles.
//Memory Usage: 36.3 MB, less than 100.00% of Kotlin online submissions for Friend Circles.
//    fun findCircleNum(M: Array<IntArray>): Int {
//        val parent = IntArray(M.size) { -1 }
//        for (i in 0 until M.size)
//            for (j in 1 until M.size) {
//                if (i != j && M[i][j] == 1) {
//                    union(parent, i, j)
//                }
//            }
//        var count = 0
//        parent.forEach { value ->
//            if (value == -1) count++
//        }
//        return count
//    }
//
//    fun union(parent: IntArray, i: Int, j: Int) {
//        val parentI = find(parent, i)
//        val parentJ = find(parent, j)
//        if (parentI != parentJ) {
//            parent[parentJ] = parentI
//        }
//    }
//
//    fun find(parent: IntArray, i: Int): Int {
//        if (parent[i] == -1) return i
//        return find(parent, parent[i])
//    }



    class DJSet(size: Int) {

        private val parent = IntArray(size) { -1 }
        private val sizes = IntArray(size) { Int.MAX_VALUE }
        var sets = 0

        fun makeSet(node: Int) {
            if (parent[node] != -1) return

            parent[node] = node
            sizes[node] = 1
            sets++
        }

        fun find(node: Int): Int {
            if (parent[node] == node) return node

            parent[node] = find(parent[node])
            return parent[node]
        }

        fun union(n1: Int, n2: Int) {
            val n1Root = find(n1)
            val n2Root = find(n2)

            if (n1Root == n2Root) return

            if (sizes[n1Root] > sizes[n2Root]) {
                parent[n1Root] = n2Root
                sizes[n1Root] = sizes[n1Root] + sizes[n2Root]
            } else {
                parent[n2Root] = n1Root
                sizes[n2Root] = sizes[n1Root] + sizes[n2Root]
            }

            sets--
        }
    }

    fun findCircleNum(M: Array<IntArray>): Int {

        val djSet = DJSet(M.size)

        for (i in 0 until M.size) {
            for (j in 0 until M[i].size) {
                if (M[i][j] == 1) {
                    djSet.makeSet(i)
                    djSet.makeSet(j)

                    djSet.union(i, j)
                }
            }
        }

        return djSet.sets
    }
}