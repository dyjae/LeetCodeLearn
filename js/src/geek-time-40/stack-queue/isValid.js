/*

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true


使用堆栈数据结构
判断最终堆栈中是否为空，空则为有效的字符串


*/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var arr = [...s]
    var stack = []
    var mapping = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for(var i = 0; i < arr.length; i++) {
        var map = mapping[arr[i]]
        if (map) {
            // ) ] }
            if (stack[stack.length - 1] === map) { // 判断栈顶是否与待入栈的是否匹配
                stack.pop()
            } else {
                return false
            }
        } else {
            // ( [ {
            stack.push(arr[i])
        }
    }
    return stack.length === 0
};

console.log(isValid('()[]{}'))

console.log(isValid('([)]'))

console.log(isValid(''))