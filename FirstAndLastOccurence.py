
# PROBLEM: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


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

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start = 0
        end = len(nums) - 1

        first = self.firstOccurence(start,end,target,nums)
        last = self.lastOccurence(start,end,target,nums)

        sol = []
        sol.extend([first, last])  # Add both elements individually

        return sol
        
