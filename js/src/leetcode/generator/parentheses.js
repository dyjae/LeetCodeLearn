/**
 * 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
 * 

    例如，给出 n = 3，生成结果为：

        [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]
    
    完全木有思路 -> 抄袭评论里的答案

 * 
 */

// TODO
const generateParenthesis = n => {
    let arr = []
    generate(arr, "", 0, 0, n)
    return arr
}
/**
 * @param {*} list 
 * @param {*} str 
 * @param {*} left 统计左括号个数
 * @param {*} right 统计右括号个数
 * @param {*} n 总括号对数
 */
const generate = (list, str, left, right, n) => {
    if (left > n || right > n) return
    if (left == n && right == n) list.push(str)
    if (left >= right) {
        generate(list, `${str}(`, left + 1, right, n)
        generate(list, `${str})`, left, right + 1, n)
    }
}

console.log(generateParenthesis(3))