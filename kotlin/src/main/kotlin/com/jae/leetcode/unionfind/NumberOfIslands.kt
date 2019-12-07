package com.jae.leetcode.unionfind

/**
 * @Description:    https://leetcode.com/problems/number-of-islands/
 * @Author Jae
 * @Date 2019-11-11 09:59
 **/

object NumberOfIslands {

    @JvmStatic
    fun main(args: Array<String>) {
        println(
            numIslands(
                arrayOf(
                    charArrayOf('1', '1', '0', '0', '0'),
                    charArrayOf('1', '1', '0', '0', '0'),
                    charArrayOf('0', '0', '1', '0', '0'),
                    charArrayOf('0', '0', '0', '1', '1')
                )
            )
        )


        println(
            numIslands(
                arrayOf(
                    charArrayOf('1', '1', '1', '1', '0'),
                    charArrayOf('1', '1', '0', '1', '0'),
                    charArrayOf('1', '1', '0', '0', '0'),
                    charArrayOf('0', '0', '0', '0', '0')
                )
            )
        )

        println(
            numIslands(
                arrayOf(
                    charArrayOf('1', '0', '1', '1', '1'),
                    charArrayOf('1', '0', '1', '0', '1'),
                    charArrayOf('1', '1', '1', '0', '1')
                )
            )
        )
    }

    //三种解法
    //1.染色体  DFS
    //Runtime: 192 ms, faster than 57.00% of Kotlin online submissions for Number of Islands.
    //Memory Usage: 36.2 MB, less than 100.00% of Kotlin online submissions for Number of Islands.
//    fun numIslands(grid: Array<CharArray>): Int {
//        var total = 0
//        val rowSize = grid.size
//        grid.forEachIndexed { rowIndex, row ->
//            val colSize = row.size
//            row.forEachIndexed { colIndex, col ->
//                if (col == '1') {
//                    total++
//                    findWords(grid, rowIndex, colIndex, rowSize, colSize)
//                }
//            }
//        }
//        return total
//    }
//
//    private fun findWords(board: Array<CharArray>, rowIndex: Int, colIndex: Int, rowSize: Int, colSize: Int) {
//        if (colIndex + 1 < colSize && board[rowIndex][colIndex + 1] == '1') change(
//            board,
//            rowIndex,
//            colIndex + 1,
//            rowSize,
//            colSize
//        )
//        if (colIndex - 1 >= 0 && board[rowIndex][colIndex - 1] == '1') change(
//            board,
//            rowIndex,
//            colIndex - 1,
//            rowSize,
//            colSize
//        )
//        if (rowIndex + 1 < rowSize && board[rowIndex + 1][colIndex] == '1') change(
//            board,
//            rowIndex + 1,
//            colIndex,
//            rowSize,
//            colSize
//        )
//        if (rowIndex - 1 >= 0 && board[rowIndex - 1][colIndex] == '1') change(
//            board,
//            rowIndex - 1,
//            colIndex,
//            rowSize,
//            colSize
//        )
//
//    }
//
//    private fun change(
//        board: Array<CharArray>,
//        rowIndex: Int,
//        colIndex: Int,
//        rowSize: Int,
//        colSize: Int
//    ) {
//        board[rowIndex][colIndex] = '0'
//        findWords(board, rowIndex, colIndex, rowSize, colSize)
//    }


    //2.染色体  BFS

    //3.并查集
    //Runtime: 204 ms, faster than 39.62% of Kotlin online submissions for Number of Islands.
    //Memory Usage: 39.3 MB, less than 100.00% of Kotlin online submissions for Number of Islands.
    fun numIslands(grid: Array<CharArray>): Int {
        if (grid.isEmpty()) return 0
        val rowSize = grid.size
        val colSize = grid[0].size
        val total = rowSize * colSize
        val uf = UnionFind(total + 1)
        val directions = arrayOf(arrayOf(0, 1), arrayOf(1, 0))
        for (row in 0 until rowSize)
            for (col in 0 until colSize) {
                val index = getIndex(colSize, row, col)
                when (grid[row][col]) {
                    '0' -> {
                        uf.union(total, index)
                    }
                    '1' -> {
                        for (d in directions) {
                            val childX = row + d[0]
                            val childY = col + d[1]
                            if (childX < rowSize && childY < colSize && grid[childX][childY] == '1') {
                                uf.union(index, getIndex(colSize, childX, childY))
                            }
                        }
                    }
                }
            }
        return uf.count - 1
    }

    fun getIndex(colSize: Int, x: Int, y: Int): Int {
        return x * colSize + y
    }

    class UnionFind(n: Int) {
        var parent: IntArray = IntArray(n)

        var rank: IntArray = IntArray(n)

        var count = n

        init {
            (0 until n).forEach {
                parent[it] = it
                rank[it] = 1
            }
        }

        fun find(p: Int): Int {
            var rootNode = p
            while (parent[rootNode] != rootNode) {
                parent[rootNode] = parent[parent[rootNode]]
                rootNode = parent[rootNode]
            }
            return rootNode
        }

        fun union(p: Int, q: Int) {
//            println("p:$p,q:$q")
            val pRoot = find(p)
            val qRoot = find(q)
            if (pRoot == qRoot) return
            when {
                rank[pRoot] > rank[qRoot] -> {
                    parent[qRoot] = pRoot
                }
                rank[pRoot] < rank[qRoot] -> {
                    parent[pRoot] = qRoot
                }
                else -> {
                    parent[qRoot] = pRoot
                    rank[pRoot] += 1
                }
            }
//            println("pRoot:${parent[pRoot]},qRoot:${parent[qRoot]}")
            count -= 1
//            println("count=$count")
        }

    }

}