# PROBLEM: https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card



class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        
        n = len(arr)
        start,end = 0,n-1
        res = -1
        
        while start <= end:
            
            mid = start + (end-start) // 2
            
            if arr[mid] == k:
                return mid
            elif k > arr[mid]:
                res = mid
                start = mid+1
            else:
                end = mid-1
                
        return res
                
                
        
        #Your code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
