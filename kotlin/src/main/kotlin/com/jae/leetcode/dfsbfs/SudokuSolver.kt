package com.jae.leetcode.dfsbfs

/**
 * https://leetcode.com/problems/sudoku-solver/
 */
fun main(args: Array<String>) {
    val array = arrayOf(
        charArrayOf('5', '3', '.', '.', '7', '.', '.', '.', '.'),
        charArrayOf('6', '.', '.', '1', '9', '5', '.', '.', '.'),
        charArrayOf('.', '9', '8', '.', '.', '.', '.', '6', '.'),
        charArrayOf('8', '.', '.', '.', '6', '.', '.', '.', '3'),
        charArrayOf('4', '.', '.', '8', '.', '3', '.', '.', '1'),
        charArrayOf('7', '.', '.', '.', '2', '.', '.', '.', '6'),
        charArrayOf('.', '6', '.', '.', '.', '.', '2', '8', '.'),
        charArrayOf('.', '.', '.', '4', '1', '9', '.', '.', '5'),
        charArrayOf('.', '.', '.', '.', '8', '.', '.', '7', '9')
    )
    solveSudoku(array)
}

//fun solveSudoku(board: Array<CharArray>) {
//    solve(board)
//}
//
//fun solve(board: Array<CharArray>): Boolean {
//    for (i in 0 until 9) {
//        for (j in 0 until 9) {
//            if (board[i][j] == '.') {
//                for (c in '1'..'9') {
//                    if (isValidate(i, j, board, c)) {
//                        board[i][j] = c
//                        if (solve(board)) {
//                            return true
//                        } else {
//                            board[i][j] = '.'
//                        }
//                    }
//                }
//                return false
//            }
//        }
//    }
//    return true
//}
//
//fun isValidate(row: Int, col: Int, board: Array<CharArray>, c: Char): Boolean {
//    for (i in 0 until 9) {
//        if (board[row][i] != '.' && board[row][i] == c) return false
//        if (board[i][col] != '.' && board[i][col] == c) return false
//        if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] != '.' &&
//            board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c
//        ) return false
//    }
//    return true
//}
//
//


fun solveSudoku(board: Array<CharArray>): Unit {

    solveDfs(board, 0, 0)

}

//深度优先遍历
fun solveDfs(board: Array<CharArray>, row: Int, col: Int): Boolean {

    if (row >= 9) return true//到了最后一行+1

    if (col >= 9) return solveDfs(board, row + 1, 0)


    if (board[row][col] == '.') {
        for (i in 1..9) {
            board[row][col] = (i + '0'.toInt()).toChar()
            if (isValidSodoku(board, row, col)) {
                if (solveDfs(board, row, col + 1)) return true
            }
            board[row][col] = '.'
        }
    } else
        return solveDfs(board, row, col + 1)

    return false
}

fun isValidSodoku(board: Array<CharArray>, row: Int, col: Int): Boolean {

    for (i in 0 until 9)
        if (i != col && board[row][col] == board[row][i]) return false
    for (i in 0 until 9)
        if (i != row && board[row][col] == board[i][col]) return false

    val m = 3 * (row / 3)
    val n = 3 * (col / 3)

    for (i in m until m + 3)
        for (j in n until n + 3)
            if ((i != row || col != j) && board[row][col] == board[i][j]) return false

    return true
}

