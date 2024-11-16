class Solution:
    def solve(self,ip, op, sol):

        if len(ip) == 0:
            sol.append(op)
            return
                 
        op1 = op
        op2 = op + [ip[0]]
        ip = ip[1:]

        self.solve(ip, op1, sol)
        self.solve(ip, op2, sol)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        self.solve(nums,[],sol)
        return sol

