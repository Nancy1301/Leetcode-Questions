# PROBLEM: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/



class Solution:

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:

            # Calculating mid
            mid = start + (end - start) // 2
            nex = (mid + 1) % n
            prev = (mid + n - 1) % n

            # Check if the mid element is the minimum
            if nums[mid] <= nums[nex] and nums[mid] <= nums[prev]:
                return nums[mid]

            elif nums[end] >= nums[mid]:
                # Right side is sorted, so search the left side
                end = mid - 1
            
            # Decide which side to search next
            elif nums[start] <= nums[mid]:
                # Left side is sorted, so search the right side
                start = mid + 1

            

            

        return -1  # Default return (shouldn't reach here in valid input)

    

