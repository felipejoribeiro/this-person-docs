from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = -1
        for i in prices:
            if i < min or min == -1:
                min = i
            if i - min > max:
                max = i - min
        return max


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
    print(s.maxProfit([7, 6, 4, 3, 1]))  # Output: 0
