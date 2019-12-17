package com.jae.leetcode.lrucache

/**
 * @Description: 146. LRU Cache   https://leetcode.com/problems/lru-cache/
 * @Author Jae
 * @Date 2019-12-13 10:05
 **/

object LRUCache {
    @JvmStatic
    fun main(args: Array<String>) {
        val cache = LRUCache(2 /* capacity */)

//        cache.put(1, 1)
//        cache.put(2, 2)
//        println(cache.get(1))       // returns 1
//        cache.put(3, 3)    // evicts key 2
//        println(cache.get(2))       // returns -1 (not found)
//        cache.put(4, 4)    // evicts key 1
//        println(cache.get(1))    // returns -1 (not found)
//        println(cache.get(3))       // returns 3
//        println(cache.get(4))       // returns 4


        cache.put(2, 1)
        cache.put(1, 1)
        cache.put(2, 3)
        cache.put(4, 1)
        println(cache.get(1))
        println(cache.get(2))
    }

    class LRUCache(private val capacity: Int) {
        val cache = LinkedHashMap<Int, Int>()

        fun get(key: Int): Int {
            val curValue = cache.remove(key) ?: return -1
            cache.put(key, curValue)
            return curValue
        }

        fun put(key: Int, value: Int) {
            if (cache.containsKey(key)) {
                cache.remove(key)
                cache[key] = value
            } else {
                if (cache.size == this.capacity) {
                    cache.remove(cache.asIterable().first().key)
                }
                cache[key] = value
            }
        }

    }

    //Runtime: 332 ms, faster than 85.71% of Kotlin online submissions for LRU Cache.
    //Memory Usage: 57.7 MB, less than 100.00% of Kotlin online submissions for LRU Cache.
//    class LRUCache(private val capacity: Int) {
//        private val cache = HashMap<Int, Node>(capacity)
//
//        private val headNode: Node = Node(0, 0)
//
//        private val tailNode: Node = Node(0, 0)
//
//        var size = 0
//
//
//        private fun addNode(node: Node) {
//            cache[node.key] = node
//            size++
//            checkPoll()
//            val headNextNode = headNode.nextNode ?: tailNode
//            headNextNode.prevNode = node
//            node.nextNode = headNextNode
//            node.prevNode = headNode
//            headNode.nextNode = node
//        }
//
//        private fun checkPoll() {
//            if (size <= capacity) return
//            val moveNode = tailNode.prevNode ?: return
//            cache.remove(moveNode.key)
//            moveNode.prevNode?.nextNode = tailNode
//            tailNode.prevNode = moveNode.prevNode
//        }
//
//        private fun moveNode(node: Node) {
//            val prevNode = node.prevNode ?: return
//            if (prevNode == headNode) return
//            val nextNode = node.nextNode ?: return
//            val headNextNode = headNode.nextNode ?: return
//            prevNode.nextNode = nextNode
//            nextNode.prevNode = prevNode
//
//            headNode.nextNode = node
//            node.prevNode = headNode
//            headNextNode.prevNode = node
//            node.nextNode = headNextNode
//        }
//
//
//        fun get(key: Int): Int {
//            return cache[key]?.let {
//                moveNode(it)
//                return@let it.value
//            } ?: -1
//        }
//
//        fun put(key: Int, value: Int) {
//            cache[key]?.let {
//                it.value = value
//                moveNode(it)
//            } ?: addNode(Node(key, value))
//        }
//
//        data class Node(val key: Int, var value: Int) {
//            var prevNode: Node? = null
//            var nextNode: Node? = null
//        }
//
//    }
}

