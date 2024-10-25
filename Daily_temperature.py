class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:

        n = len(t)
        v = [-1] * n
        st = []
        res = [0] * n

        for i, num in enumerate(reversed(t)):

            while st and t[st[-1]] <= num:
                st.pop()

            if st:

                v[n-1-i] = st[-1]

            st.append(n-1-i)
            
        
        for i in range(n):
            if v[i] != -1:  # If there is a warmer day, calculate the difference
                res[i] = v[i] - i
            else:
                res[i] = 0
        return res




        
