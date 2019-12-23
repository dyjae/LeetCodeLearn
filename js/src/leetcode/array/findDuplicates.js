/*
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]

条件：1 ≤ a[i] ≤ n （n为数组长度）
    1 -> i=0
    2 -> i=1
    3 -> i=2
    ...

交换两个变量的值，例如 a 和 b，不使用第三个变量，有两种不同的方法：
    基于异或运算	 基于加减法
    a = a ^ b       a = a + b
    b = a ^ b       b = a - b
    a = a ^ b	    a = a - b

 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */

var findDuplicates = function(nums) {
    var result = []
    var len = nums.length
    if (len >= 2) {
        for (var i = 0; i < len; i++) {
            // 当前值应该所在位置的值 !== 当前值
            while (nums[nums[i] - 1] !== nums[i]) {
                swap(nums, i, nums[i] - 1)
            }
        }
        for (var i = 0; i < len; i++) {
            if (nums[i] - 1 !== i) {
                result.push(nums[i])
            }
        }
    }
    return result
};

// 数值交换
var swap = function (nums, i1, i2) {
    if (i1 == i2) return
    nums[i1] = nums[i1] + nums[i2]
    nums[i2] = nums[i1] - nums[i2]
    nums[i1] = nums[i1] - nums[i2]
}

// var findDuplicates = function(nums) {
//     var result = []
//     if (nums.length >= 2) {
//         for (var i = 0; i < nums.length; i++) {
//             for (var j = i + 1; j < nums.length; j++) {
//                 if (nums[i] === nums[j]) {
//                     result.push(nums[i])
//                     break
//                 }
//             }
//         }
//     }
//     return result
// };

console.log(findDuplicates([4,3,2,7,8,2,3,1]))