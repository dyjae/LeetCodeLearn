package com.jae.leetcode.dfsbfs

/**
 * @Description: https://leetcode.com/problems/n-queens/
 * @Author yj
 * @Date 2019-08-15 18:38
 **/
fun main(args: Array<String>) {
    println(totalNQueens(4))
}

//Runtime: 192 ms, faster than 33.33% of Kotlin online submissions for N-Queens II.
//Memory Usage: 35.3 MB, less than 100.00% of Kotlin online submissions for N-Queens II.
//fun totalNQueens(n: Int): Int {
//    val rs = arrayOf(0)
//    dfs(
//        1, n, emptySet<Int>().toMutableSet(), emptySet<Int>().toMutableSet(),
//        emptySet<Int>().toMutableSet(), rs
//    )
//    return rs[0]
//}
//
//fun dfs(
//    row: Int,
//    n: Int,
//    p: MutableSet<Int>,
//    na: MutableSet<Int>,
//    col: MutableSet<Int>,
//    rs: Array<Int>
//) {
//    if (row > n) {
//        rs[0] = rs[0] + 1
//        return
//    }
//    var exit = false
//    for (i in 1..n) {//列的循环
//        if (col.contains(i) || p.contains(row + i) || na.contains(row - i)) continue
//        col.add(i)
//        p.add(row + i)
//        na.add(row - i)
//        exit = true
//        dfs(row + 1, n, p, na, col, rs)//行的递归（处理每一行的结果）
//        col.remove(i)
//        p.remove(row + i)
//        na.remove(row - i)
//    }
//    if (!exit) return
//}

fun totalNQueens(n: Int): Int {
    var result = 0
    loopFind(IntArray(n), 0) {
        result++
    }
    return result
}

private fun loopFind(queenPosArr: IntArray, queueColumn: Int,
                     callback: () -> Unit) {
    // 尝试在当前行的每一列放置，first 为第几列（x），second 为第几行（y）
    for (row in 0 until queenPosArr.size) {
        var isRowRight = true
        for (i in 0 until queueColumn) { // 对比之前的位置是否合法
            if (isPosConflict(queenPosArr[i], i, row, queueColumn)) {
                isRowRight = false
                break
            }
        }
        if (isRowRight) {
            queenPosArr[queueColumn] = row
            if (queueColumn >= queenPosArr.size - 1) { // 已经配置全了
                callback()
            } else {
                loopFind(queenPosArr, queueColumn + 1, callback)
            }
        }
    }
}

private fun isPosConflict(x1: Int, y1: Int, x2: Int, y2: Int) =
    x1 == x2 || y1 == y2 || Math.abs((x1 - x2).toDouble() / (y1 - y2).toDouble()) == 1.0


