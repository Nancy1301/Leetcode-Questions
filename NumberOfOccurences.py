# PROBLEM: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card



class Solution:
    
    def firstOccurence(self,start,end,target,nums):

        first = -1
        while start <= end:

            mid = (start + end) // 2

            if target == nums[mid]:
                first = mid
                end = mid-1
            
            elif target < nums[mid]:
                end = mid-1
            else:
                start = mid + 1

        return first

    def lastOccurence(self,start,end,target,nums):

        last = -1
        while start <= end:

            mid = (start + end) // 2

            if target == nums[mid]:
                last = mid
                start = mid+1
            
            elif target < nums[mid]:
                end = mid-1
            else:
                start = mid + 1

        return last
        
    def countFreq(self, nums, target):
        #code here
        
        start = 0
        end = len(nums) - 1
        
        first = self.firstOccurence(start,end,target,nums)
        if first == -1:  # Target not found
            return 0
        last = self.lastOccurence(start,end,target,nums)
 
        return (last - first) + 1
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
