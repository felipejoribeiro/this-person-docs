---
id: search_insert_position
aliases: []
tags: []
---

## Problem's summary:

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

## Responses:

### My authoral response:

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
```

### Binary search response:

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            midpoint = (left + right) // 2
            if list[midpoint] == target:
                return midpoint
            elif target > nums[midpoint]:
                left = midpoint + 1
            else:
                right = midpoint -1
        return left
```

This problam had unreliable memory and time readings. Probably due to too small test cases, i'm not sure, but the results didn't make sense.
