#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    # Function to calculate the span of stock's price for all n days.
    def calculateSpan(self, arr):
        #write code here
        n = len(arr)
        v = [-1]* n
        st = []
        res = [0]*n
        
        for i, num in enumerate(arr):
            
            while st and arr[st[-1]] <= num:
                st.pop()
            if st:
                v[i] = st[-1]
            
            st.append(i)
        
        for i in range(n):
            res[i] = i - v[i] 
            
        return res    
        
        
        
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        # print("~")
        t -= 1
# } Driver Code Ends
