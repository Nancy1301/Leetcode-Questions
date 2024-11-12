#User function Template for python3

from typing import List

class Solution:
    
    def insert(self,St,temp):
        if len(St) == 0:
            St.append(temp)
            return
        
        val = St.pop()
        self.insert(St, temp)
        St.append(val)

    def reverse(self,St): 
        
        # base condition:
        if len(St) == 1:
            return
        temp = St[-1]
        
        St.pop()
        self.reverse(St)
        self.insert(St, temp)
        return
        
        #code here


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
    print("~")
# } Driver Code Ends
