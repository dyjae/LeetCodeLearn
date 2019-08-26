package com.jae.leetcode.trie

/**
 * @description https://leetcode.com/problems/implement-trie-prefix-tree/
 * @author Jae
 * @date 2019-08-26 10:32
 */
fun main(args: Array<String>) {
    val trie = Trie()

    trie.insert("a")
    println(trie.search("a"))
    println(trie.startsWith("a"))
}



//Runtime: 348 ms, faster than 85.71% of Kotlin online submissions for Implement Trie (Prefix Tree).
//Memory Usage: 49 MB, less than 100.00% of Kotlin online submissions for Implement Trie (Prefix Tree).
class Trie() {

    /** Initialize your data structure here. */
    private val root = TrieNode(' ', false)

    /** Inserts a word into the trie. */
    fun insert(word: String) {
        var trie = root
        word.forEach { c ->
            val newTrie = trie.child[c - 'a'] ?: TrieNode(c)
            trie.child[c - 'a'] = newTrie
            trie = newTrie
        }
        trie.isEnd = true
    }

    /** Returns if the word is in the trie. */
    fun search(word: String): Boolean {
        var trie = root
        word.forEach { c ->
            trie = trie.child[c - 'a'] ?: return false
        }
        return trie.isEnd
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    fun startsWith(prefix: String): Boolean {
        var trie = root
        prefix.forEach { c ->
            trie = trie.child[c - 'a'] ?: return false
        }
        return true
    }


    data class TrieNode(val value: Char, var isEnd: Boolean = false) {
        val child: Array<TrieNode?> = arrayOfNulls(26)
    }

}


//332
//class Trie() {
//
//    /** Initialize your data structure here. */
//    class TrieNode {
//        var isTire = false
//        var children = arrayOfNulls<TrieNode>(26)
//    }
//
//    var root = TrieNode()
//
//    /** Inserts a word into the trie. */
//    fun insert(word: String) {
//        var p = root
//        for (item in word) {
//            val index = item.toLowerCase().toInt()-'a'.toInt()
//            if (p.children[index] == null) {
//                p.children[index] = TrieNode()
//            }
//            p = p.children[index]!!
//        }
//        p.isTire = true
//    }
//
//    /** Returns if the word is in the trie. */
//    fun search(word: String): Boolean {
//        val findWord = findWord(word)
//        return findWord!=null && findWord.isTire
//    }
//
//    /** Returns if there is any word in the trie that starts with the given prefix. */
//    fun startsWith(prefix: String): Boolean {
//        return findWord(prefix)!=null
//    }
//    fun findWord(word:String):TrieNode?{
//        var p = root
//        for (itemChar in word) {
//            val index = itemChar.toLowerCase().toInt()-'a'.toInt()
//            if (p.children[index] == null){
//                return null
//            }
//            p = p.children[index]!!
//        }
//        return p
//    }
//}
