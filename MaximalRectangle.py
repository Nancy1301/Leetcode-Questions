class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nsr_index = [0]*n
        nsl_index = [0]*n
        st = []
        st1 = []

        # Finding nearest smaller to left element's index
        for index in range(n):
            while st and heights[st[-1]] >= heights[index]:
                st.pop()
            if st:
                nsr_index[index] = st[-1]
            else:
                nsr_index[index] = -1 
            st.append(index)

        # Finding nearest smaller to right element's index
        for index in range(n - 1, -1, -1):
            while st1 and heights[st1[-1]] >= heights[index]:
                st1.pop()
            if st1:
                nsl_index[index] = st1[-1]
            else:
                nsl_index[index] = n
            st1.append(index)   
            
        # Find (difference of these indexes-1)* array's element
        num = 0
        for i in range(n):
            area = (nsl_index[i] - nsr_index[i]-1) * heights[i]
            num = max(num, area)
            
        return num
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        # Ensure that matrix is not empty
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        # Iterate over each row in the matrix
        for row in matrix:
            # Update heights array
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Calculate max area for the current histogram (heights)
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area
