"""
Given an integer array nums and an integer k, return true if there are two
distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105
"""

from typing import List


class Solution:
    """Answered using Sliding Window"""

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0
        counter = {}
        counter[nums[0]] = 1

        while right < len(nums) - 1:
            right += 1
            if counter.get(nums[right]):
                counter[nums[right]] += 1
            else:
                counter[nums[right]] = 1
            while counter[nums[right]] == 2:
                if abs(left - right) <= k:
                    return True
                else:
                    counter[nums[left]] -= 1
                left += 1

        return False


class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i

        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))

s2 = Solution()
print(s2.containsNearbyDuplicate([1, 0, 1, 1], 1))
