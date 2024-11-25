# PROBLEM: https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:

    def solve(self, vec, k, index) -> int:

        if len(vec) == 1:
            return vec[0]
        index = (index + k) % len(vec)
        del vec[index]

        ans = self.solve(vec, k, index)
        return ans


    def findTheWinner(self, n: int, k: int) -> int:

        vec = []
        for i in range(n):
            vec.append(i+1)
        k -=1
        index = 0
        ans = self.solve(vec, k, index)

        return ans








        
