package com.jae.leetcode.trie

/**
 * @Description: https://leetcode.com/problems/word-search-ii/
 * @Author Jae
 * @Date 2019-08-27 09:22
 **/

fun main(args: Array<String>) {
    val board = arrayOf(
        charArrayOf('o', 'a', 'a', 'n'),
        charArrayOf('e', 't', 'a', 'e'),
        charArrayOf('i', 'h', 'k', 'r'),
        charArrayOf('i', 'f', 'l', 'v')
    )
    val words = arrayOf("oath", "pea", "eat", "rain")
    findWords(board, words).forEach {
        println(it)
    }
}


//Runtime: 324 ms, faster than 94.12% of Kotlin online submissions for Word Search II.
//Memory Usage: 51.8 MB, less than 100.00% of Kotlin online submissions for Word Search II.
fun findWords(board: Array<CharArray>, words: Array<String>): List<String> {
    //1.将单词放到一个字典树中
    val trie = Trie()
    words.forEach {
        trie.insert(it)
    }
    val rs = emptySet<String>().toMutableSet()
    for (i in 0 until board.size) {
        for (j in 0..board[i].size) {
            dfs(i, j, board, "", trie, Array(board.size) { BooleanArray(board[i].size) }, rs)
        }
    }

    return rs.toList()
}

fun dfs(
    x: Int,
    y: Int,
    board: Array<CharArray>,
    str: String,
    trie: Trie,
    visit: Array<BooleanArray>,
    rs: MutableSet<String>
) {
    if (x >= board.size || y >= board[x].size || visit[x][y]) return //过线或访问过了
    val char = board[x][y]
    val newStr = str + char
    if (!trie.startsWith(newStr)) return //该词不能组成前缀
    if (trie.search(newStr)) {
        rs.add(newStr)
    }
    visit[x][y] = true
    dfs(x + 1, y, board, newStr, trie, visit, rs)//下
    dfs(x, y + 1, board, newStr, trie, visit, rs)//右
    if (y - 1 >= 0) {
        dfs(x, y - 1, board, newStr, trie, visit, rs)//左
    }
    if (x - 1 >= 0) {
        dfs(x - 1, y, board, newStr, trie, visit, rs)//上
    }
    visit[x][y] = false
}