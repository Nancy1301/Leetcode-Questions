# PROBLEM: Print N-bit binary numbers having more 1s than 0s


#User function Template for python3
class Solution:
    
    def solve(self, one, zero, op, n):
        
        if n==0:
            print(op, end=" ")
            return
        
        op1 = op + "1"
        self.solve(one+1, zero, op1, n-1)
        
        if one>zero:
            op2 = op + "0"
            self.solve(one, zero+1, op2, n-1)
    
    
    
	def NBitBinary(self, n):
		# code here
		
		op = ""
		one = 0
		zero = 0
		
		self.solve(one, zero, op, n)
		
		return op
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        answer = ob.NBitBinary(n)
        for value in answer:
            print(value, end=" ")
        print()
        print("~")

# } Driver Code Ends
