class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products
        pre_prod = 1
        for i in range(n):
            answer[i] = pre_prod
            pre_prod *= nums[i]
        
        # Calculate suffix products and multiply with prefix
        suf_prod = 1
        for i in range(n - 1, -1 , -1):
            answer[i] *= suf_prod
            suf_prod *= nums[i]
        
        return answer
        
