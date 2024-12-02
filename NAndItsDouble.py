# PROBLEM: https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=daily-question&envId=2024-12-01

1346. Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for num in arr:

            if num*2 in seen or (num // 2 in seen and num%2==0):
                return True
        
            seen.add(num)
        return False

