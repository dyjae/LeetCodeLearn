/**
 * 实现 pow(x, n) ，即计算 x 的 n 次幂函数
 *  

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

 * 
 */

/**
 * pow(2, -2147483648) -> 超出时间限制 -> 不方案可行！
 */
const pow = (x, n) => {
    /*
        // es6
        return x ** n
    */
    if (n == 0) return 1
    if (n < 0) {
        n *= -1
        x = 1 / x
    }
    let result = x
    while (n != 1) {
        result = result * x
        n--
    }
    return result
}
console.log(`pow(2, 10) -> ${pow(2, 10)}`)
console.log(`pow(2.1, 3) -> ${pow(2.1, 3)}`)
console.log(`pow(2, -2) -> ${pow(2, -2)}`)