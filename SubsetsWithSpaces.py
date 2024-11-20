# Problem: https://www.geeksforgeeks.org/problems/permutation-with-spaces3627/1



#User function Template for python3


class Solution:


    def solve(self, ip,op,sol):
        
        if len(ip) == 0:
            sol.append(op)
            return
        
        op1 = op + " " + ip[0]
        op2 = op + ip[0]
        
        ip = ip[1:]
        
        self.solve(ip,op1,sol)
        self.solve(ip,op2,sol)

    def permutation(self, s):
        # code here
        sol = []
        op = s[0]
        ip = s[1:]
        
        self.solve(ip,op,sol)
        
        return sol
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        S = input()
        ans = ob.permutation(S)
        write = ""
        for i in ans:
            write += "(" + i + ")"
        print(write)

        print("~")
# } Driver Code Ends
