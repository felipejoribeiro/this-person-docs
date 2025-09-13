---
id: find_the_duplicate_number
aliases: []
tags: []
---

## Problem's summary:

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

## Responses:

Started popping a number out and converting to set to check if the length changes. It solved the problem but was too slow and wasn't approved.

### Best time complexity:

```python
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [-1]*(len(nums)+1)
        for i in nums:
            if arr[i]!=-1:
                return i
            else:
                arr[i] = i
```

### Best space complexity:

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        p = 0
        while True:
            if nums[i] == 0:
                return p
            p = nums[i]
            nums[i] = 0
            i = p
```
