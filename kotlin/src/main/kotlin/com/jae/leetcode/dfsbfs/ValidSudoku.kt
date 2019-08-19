package com.jae.leetcode.dfsbfs

/**
 * @Description: https://leetcode.com/problems/valid-sudoku/
 * @Author yj
 * @Date 2019-08-17 10:15
 **/
fun main(args: Array<String>) {
//    [['5','3','.','.','7','.','.','.','.'],
//        ['6','.','.','1','9','5','.','.','.'],
//        ['.','9','8','.','.','.','.','6','.'],
//        ['8','.','.','.','6','.','.','.','3'],
//        ['4','.','.','8','.','3','.','.','1'],
//        ['7','.','.','.','2','.','.','.','6'],
//        ['.','6','.','.','.','.','2','8','.'],
//        ['.','.','.','4','1','9','.','.','5'],
//        ['.','.','.','.','8','.','.','7','9']]

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
//    val array = arrayOf(
//        charArrayOf('.', '.', '.', '.', '5', '.', '.', '1', '.'),
//        charArrayOf('.', '4', '.', '3', '.', '.', '.', '.', '.'),
//        charArrayOf('.', '.', '.', '.', '.', '3', '.', '.', '1'),
//        charArrayOf('8', '.', '.', '.', '.', '.', '.', '2', '.'),
//        charArrayOf('.', '.', '2', '.', '7', '.', '.', '.', '.'),
//        charArrayOf('.', '1', '5', '.', '.', '.', '.', '.', '.'),
//        charArrayOf('.', '.', '.', '.', '.', '2', '.', '.', '.'),
//        charArrayOf('.', '2', '.', '9', '.', '.', '.', '.', '.'),
//        charArrayOf('.', '.', '4', '.', '.', '.', '.', '.', '.')
//    )
    println(isValidSudoku(array))
}

//Runtime: 252 ms, faster than 8.64% of Kotlin online submissions for Valid Sudoku.
//Memory Usage: 38.8 MB, less than 100.00% of Kotlin online submissions for Valid Sudoku.
//fun isValidSudoku(board: Array<CharArray>): Boolean {
//    //列
//    val colMap = emptyMap<Int, MutableSet<Char>>().toMutableMap()
//    //格子
//    val gridMap = emptyMap<Int, MutableMap<Int, MutableSet<Char>>>().toMutableMap()
//
//    //列遍历
//    board.forEachIndexed { rowIndex, rowChars ->
//        //行遍历
//        val set = emptySet<Char>().toMutableSet()
//        rowChars.forEachIndexed { colIndex, char ->
//            //整行判断重复
//            if (char != '.' && set.contains(char)) {
//                println("行：rowIndex:$rowIndex,colIndex:$colIndex,char:$char")
//                return false
//            }
//            //竖行判断重复
//            val colSet = colMap[colIndex] ?: emptySet<Char>().toMutableSet()
//            if (char != '.' && colSet.contains(char)) {
//                println("列：rowIndex:$rowIndex,colIndex:$colIndex,char:$char")
//                return false
//            }
//            //九宫格判断重复
//            val gridSetMap = gridMap[rowIndex / 3] ?: emptyMap<Int, MutableSet<Char>>().toMutableMap()
//            val gridSet = gridSetMap[colIndex / 3] ?: emptySet<Char>().toMutableSet()
//            gridSetMap[colIndex / 3] = gridSet
//            gridMap[rowIndex / 3] = gridSetMap
//            if (char != '.' && gridSet.contains(char)) {
//                println("格子：rowIndex:$rowIndex,colIndex:$colIndex,char:$char")
//                return false
//            }
//            colSet.add(char)
//            set.add(char)
//            gridMap[rowIndex / 3]!![colIndex / 3]!!.add(char)
//            colMap[colIndex] = colSet
//        }
//    }
//    return true
//}


fun isValidSudoku(board: Array<CharArray>): Boolean {
    for (i in 0 until board.size) {
        if (!board.valid(i)) {
            return false
        }
    }
    return true
}

fun Array<CharArray>.valid(i: Int): Boolean {
    val ix = (i / 3) * 3
    val jx = (i % 3) * 3
    return this.isValid { this[i][it] } &&//判断横向
            this.isValid { this[it][i] } &&//判断竖向
            this.isValid { this[it / 3 + ix][it % 3 + jx] }//判断九宫格
}

fun Array<CharArray>.isValid(getter: (Int) -> Char): Boolean {
    var valid = 0
    for (i in 0 until this.size) {
        val c = getter(i)
        if (c != '.') {//每个字符都会占一位，判断那一位是否占了
            val mask: Int = 1 shl (c.toInt() - 26)//数字的ascall从26开始
            if ((valid and mask) == mask) return false//与运算比较
            valid = valid or mask//或运算加值
        }
    }
    return true
}
