/*
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

[1,2,3]
1 2,3
2 1,3
3 1,2
1,2,3

[1,2,3,4]
1 2,3,4
2 1,3,4
3 1,2,4
4 1,2,3

*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  var result = []
  backtrack(0, nums, result, [])
  return result
}
function backtrack(i, nums, result, tmp) {
  result.push([...tmp])
  for(var j = i; j < nums.length; j++) {
    tmp.push(nums[j])
    backtrack(j + 1, nums, result, tmp)
    tmp.pop()
  }
}


// var subsets = function (nums) {
//   var result = []
  
//   for (var i = 0; i < nums.length; i++) {
//     result.push([nums[i]])
//     var subs = []
//     for (var j = 0; j < nums.length; j++) {
//       if (i !== j) {
//         subs.push(nums[j])
//       }
//     }
//     if (subs.length > 1) result.push(subs)
//     if (subs.length > 2) {
//       getSubs(result, subs)
//     }
//   }

//   result.push([])
//   if (nums.length > 1) {
//     result.push(nums)
//   }
//   return result
// };
// function getSubs(result, subs) {
//   for (var i = 0; i < subs.length; i++) {
//     var tmps = []
//     for (var j = 0; j < subs.length; j++) {
//       if (i !== j) {
//         tmps.push(subs[j])
//       }
//     }
//     if (tmps.length > 0) result.push(tmps)
//     if (tmps.length > 2) {
//       getSubs(result, tmps)
//     }
//   }
// }

console.log(subsets([0]))

console.log(subsets([1, 2]))

console.log(subsets([1, 2, 3]))

console.log(subsets([1, 2, 3, 4]))

console.log(subsets([1, 2, 3, 4, 5]))