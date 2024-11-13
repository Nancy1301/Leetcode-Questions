class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if(n==1 and k==1):
            return 0

        # taking mid of the length of rows
        mid = (2 ** (n-1)) / 2

        if k <= mid:
            return int(self.kthGrammar(n-1,k))
        else:
            return int(not self.kthGrammar(n-1,k-mid))
             


        
