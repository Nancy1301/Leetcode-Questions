# Problem: https://leetcode.com/problems/subsets-ii/description/

class Solution:

    def solve(self,ip, op, sol):
        if len(ip) == 0:
            sol.add(tuple(op)) # converting op as tuple because sets in Python cannot store mutable types like lists. Tuples, however, are immutable and hashable, making them compatible with sets.
            return       
        op1 = op
        op2 = op + [ip[0]]
        ip = ip[1:] # creating a new list that contains all the elements of the list ip except for the first one

        self.solve(ip, op1, sol)
        self.solve(ip, op2, sol)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Why sorting it ?
        sol = set()
        self.solve(nums,[],sol)
        # sol = sorted(sol) # When we need to throw the output in a lexigraphical manner
        return list(sol)

        

        
