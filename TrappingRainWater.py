class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        water = [0]*n
        maxL = [0]*n
        maxR = [0]*n
    
        # Let's find the maximum to the left element
        init_left_val  = height[0]
        maxL[0] =init_left_val

        for i in range(1, n):
            init_left_val = max(init_left_val,height[i])
            maxL[i] = init_left_val
        

        # Let's find the maximum to the right element
        init_right_val  = height[n-1]
        maxR[n-1] = init_right_val

        for i in range(n-2, -1,-1):
            init_right_val = max(init_right_val, height[i])
            maxR[i] = init_right_val
        
        # Let's find the minimum of each height's difference and subtract from the height 

        total_water = 0
        for i in range(n):
            water[i] = min(maxL[i], maxR[i]) - height[i]
            total_water += water[i]
        # print(total_water)

        return total_water
