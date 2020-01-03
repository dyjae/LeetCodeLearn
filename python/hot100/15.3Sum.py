# 遍历得到一个数是k   而需要的另外的数为 sum = 0-k
from typing import List


class ThreeSum:

    # Runtime: 1752 ms, faster than 17.60% of Python3 online submissions for 3Sum.
    # Memory Usage: 15.6 MB, less than 100.00% of Python3 online submissions for 3Sum.
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        rs = set()
        if len(nums) < 3: return rs
        nums = sorted(nums)
        if not nums or nums[0] > 0 or nums[-1] < 0: return rs
        if nums[-1] == 0 and nums[-1] == nums[-3]: return [[0, 0, 0]]
        for index in range(len(nums)):
            head, tail, target = index + 1, len(nums) - 1, 0 - nums[index]
            while head < tail:
                if nums[head] + nums[tail] == target:
                    rs.add((nums[index], nums[head], nums[tail]))
                    head += 1
                    tail -= 1
                elif nums[head] + nums[tail] > target:
                    tail -= 1
                else:
                    head += 1
        return list(rs)


nums = [-2, 0, 1, 1, 2]
print(ThreeSum.threeSum(nums))
