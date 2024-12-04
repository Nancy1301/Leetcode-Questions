# PROBLEM: https://leetcode.com/problems/adding-spaces-to-a-string/?envType=daily-question&envId=2024-12-03

2109. Adding Spaces to a String


class Solution:
    def addSpaces(self, s: str, a: List[int]) -> str:
        
        j=0
        ans = ""
        n = len(s)
        for i in range(n):
            if j < len(a) and i < a[j]:
                ans = ans + s[i]
            elif j < len(a) and i == a[j]:
                ans = ans + " " + s[i]
                j += 1
            else:
                ans = ans + s[i]
        
        return ans
