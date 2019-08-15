/**
 * 求众数
 *  给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
 */


const majorityElement = (nums) => {

    // 算法题，尽量减少使用api
    return nums.sort()[parseInt(nums.length / 2)]

    
}

console.log(majorityElement([2, 2, 1, 1, 1, 2, 2]))
console.log(majorityElement([3,2,3]))