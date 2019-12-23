/**
 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

 示例 1:
 输入: [4,2,3]
 输出: True
 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

 示例 2:
 输入: [4,2,1]
 输出: False
 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

 说明:  n 的范围为 [1, 10,000]。

     x    y   z
     1    3   2
     2    3   1
     3    3   1
     2    3   2
     要满足条件，需要如下调整：
     1，当x<z,让y=z
     2，当x>z,让z=y
     3, 当x=z,让y=z
     综合以上可以得到：当x存在且x>z，就让z=y，否则让y=z

 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
let checkPossibility = function(nums) {
    if (nums.length < 3) return true; // 只有两位数时，必然可以变非递减数列
    let count = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i + 1] < nums[i]) {
            count++;
            if (count > 1) return false
            if (i > 0 && nums[i - 1] > nums[i + 1]) nums[i + 1] = nums[i]
        }
    }
    return true;
};

let nums = [4, 2, 3]
console.log(checkPossibility(nums))
nums = [4, 2, 1]
console.log(checkPossibility(nums))
nums = [3, 4, 2, 3]
console.log(checkPossibility(nums))