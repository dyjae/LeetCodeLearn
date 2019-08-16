package com.jae.leetcode.dfsbfs

/**
 * @Description: https://leetcode.com/problems/n-queens/
 * @Author yj
 * @Date 2019-08-15 18:38
 **/
fun main(args: Array<String>) {
    solveNQueens(4).forEach {
        it.forEach(::println)
        println()
    }

}

//Runtime: 224 ms, faster than 55.56% of Kotlin online submissions for N-Queens.
//Memory Usage: 38.1 MB, less than 100.00% of Kotlin online submissions for N-Queens.
//fun solveNQueens(n: Int): List<List<String>> {
//    val rs = emptyList<MutableList<String>>().toMutableList()
//    dfs(
//        1, n, emptySet<Int>().toMutableSet(), emptySet<Int>().toMutableSet(),
//        emptySet<Int>().toMutableSet(), rs, emptyList<String>().toMutableList()
//    )
//    return rs
//}
//
//fun dfs(
//    row: Int,
//    n: Int,
//    p: MutableSet<Int>,
//    na: MutableSet<Int>,
//    col: MutableSet<Int>,
//    rs: MutableList<MutableList<String>>,
//    temp: MutableList<String>
//) {
//    if (row > n) {
//        val temprs = emptyList<String>().toMutableList()
//        temp.forEach { temprs.add(it) }
//        rs.add(temprs)
//        return
//    }
//    var exit = false
//    for (i in 1..n) {//列的循环
//        if (col.contains(i) || p.contains(row + i) || na.contains(row - i)) continue
//        col.add(i)
//        p.add(row + i)
//        na.add(row - i)
//        val str = getStr(i, n)
//        temp.add(str)
//        exit = true
//        dfs(row + 1, n, p, na, col, rs, temp)//行的递归（处理每一行的结果）
//        col.remove(i)
//        p.remove(row + i)
//        na.remove(row - i)
//        temp.remove(str)
//    }
//    if (!exit) return
//}
//
//fun getStr(i: Int, n: Int): String {//生成每一行的串
//    var rs = ""
//    for (index in 1 until i) {
//        rs += "."
//    }
//    rs += "Q"
//    if (i != n) {
//        for (index in i + 1..n) {
//            rs += "."
//        }
//    }
//    return rs
//}

//188
fun solveNQueens(n: Int): List<List<String>> {
    val result = ArrayList<List<String>>()
    loopFind(IntArray(n), 0) {
        val cell = ArrayList<String>()
        it.forEachIndexed { _, row ->
            val column = StringBuilder()
            for (i in 0 until n) {
                column.append(if (row != i) '.' else 'Q')
            }
            cell.add(column.toString())
        }
        result.add(cell)
    }
    return result
}

private fun loopFind(
    queenPosArr: IntArray, queueColumn: Int,
    callback: (queenRowArr: IntArray) -> Unit
) {
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
                callback(queenPosArr)
            } else {
                loopFind(queenPosArr, queueColumn + 1, callback)
            }
        }
    }
}

private fun isPosConflict(x1: Int, y1: Int, x2: Int, y2: Int) =
    x1 == x2 || y1 == y2 || Math.abs((x1 - x2).toDouble() / (y1 - y2).toDouble()) == 1.0