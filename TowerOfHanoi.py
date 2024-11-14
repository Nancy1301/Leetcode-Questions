# User function Template for python3

class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # Your code here
        
        if n==0:
            return 0
        if n==1:
            return 1
            
        count = self.towerOfHanoi(n-1,fromm,aux,to)
        count+=1
        count+= self.towerOfHanoi(n-1,aux,to,fromm)
        
        return count


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.towerOfHanoi(N, 1, 3, 2))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
