# Problem: https://leetcode.com/problems/letter-case-permutation/description/


class Solution:

    def solve(self, ip, op, sol):

        if len(ip) == 0:
            sol.append(op)
            return
        
        if ip[0].isalpha():

            op1 = op + ip[0].lower()
            op2 = op + ip[0].upper()
            ip = ip[1:]  # Remove the first character
            self.solve(ip, op1, sol)
            self.solve(ip, op2, sol)
        else:
            # If it's not a letter (e.g., a digit), include it in `op` directly
            op = op + ip[0]
            ip = ip[1:]  # Remove the first character
            self.solve(ip, op, sol)

    def letterCasePermutation(self, s: str) -> List[str]:

        sol = []
        self.solve(s, "", sol)
        return sol


        
