Problem: https://leetcode.com/problems/generate-parentheses/description/


class Solution:
    def solve(self, op, cl, out, solution):
        if op == 0 and cl == 0:
            solution.append(out)
            return

        # Add an opening parenthesis if there are any left
        if op > 0:
            out1 = out + "("
            self.solve(op - 1, cl, out1, solution)

        # Add a closing parenthesis if it would not unbalance the string
        if cl > op:
            out2 = out + ")"
            self.solve(op, cl - 1, out2, solution)

    def generateParenthesis(self, n: int):
        solution = []
        op = n
        cl = n
        out = ""
        self.solve(op, cl, out, solution)
        return solution

