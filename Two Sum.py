class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab = {}
        n = len(nums)

        for i in range(n):
            tab[nums[i]] = i       # key - number ; value - times it came
            # 2-0
            7-1
            11-2
            15-3 #
            
        for i in range(n):
            value = target - nums[i] #. 9 - 2 = 7
            if value in tab and tab[value] != i:    # 1 != 0
                return [i, tab[value]] # 0, 1
        
        return []                       # 3 - 0 ; 2 - 1; 4 - 2
            
        
