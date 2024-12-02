# PROBLEM: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

744. Find Smallest Letter Greater Than Target


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        start, end = 0, n-1
        res = letters[0]

        while start <= end:
            mid = start + (end-start) // 2

            if letters[mid] <= target:
                start = mid + 1 

            elif letters[mid] > target:
                res = letters[mid]
                end = mid-1                

        return res
