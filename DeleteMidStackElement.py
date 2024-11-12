class Solution:
  
    def solve(self,s,mid):
        if mid == 1:
            s.pop()
            return
        temp = s.pop()
        # Recursively call solve with mid - 1
        self.solve(s, mid - 1)
        
        # After reaching the middle, push the popped elements back to maintain the original stack
        s.append(temp)
        return
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        
        mid = ((sizeOfStack) // 2 ) + 1
        
        self.solve(s,mid)


