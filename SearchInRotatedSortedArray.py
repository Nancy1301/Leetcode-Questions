# PROBLEM: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:
    
            mid = start + (end - start) // 2
            if t == nums[mid]:
                return mid

            # THIS IS TO CHECK THAT LEFT SIDE IS SORTED AS WE NEED TO CHECK ONLY IN THE SORTED
            if nums[mid] >= nums[start]:
                if nums[start] <= t < nums[mid]: # Checking in which side (left or right) target value falls
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[mid] < t <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
    
        return -1 
        
