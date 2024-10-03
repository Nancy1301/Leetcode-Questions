class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = {}

        for num in nums:
            if num not in dup:
                dup[num] = 1
            else:
                return True # only because whatever be the other case, it would show duplicacy 
        return False
        
