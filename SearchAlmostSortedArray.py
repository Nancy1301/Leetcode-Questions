
# PROBLEM: https://www.geeksforgeeks.org/problems/search-in-an-almost-sorted-array/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

class Solution:
    def findTarget(self, nums, t):
        # Your code here
        n = len(arr)
        start = 0
        end = n-1
        
        while start <= end:
    
            mid = start + (end - start) // 2
            if t == nums[mid]:
                return mid
            elif mid > start and t == nums[mid-1]: # if the 0th element is mid then mid-1 would throw index out of bound error
                return mid-1
            elif mid < end and t == nums[mid+1]:
                return mid+1
            elif t < nums[mid]:
                end = mid-2
            elif t > nums[mid]:
                start = mid+2
    
        
        return -1


if __name__ == "__main__":
    t = int(input())  # Number of test cases

    for _ in range(t):
        arr = list(map(int, input().strip().split()))  # Read the array
        target = int(input().strip())  # Read the target

        sln = Solution()
        ans = sln.findTarget(arr, target)
        print(ans)
        print("~")
