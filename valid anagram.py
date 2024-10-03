class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}

        # Iterate through both strings simultaneously
        for ch_s, ch_t in zip_longest(s, t):
            if ch_s:  # If character from s is not None
                if ch_s not in first:
                    first[ch_s] = 1
                else:
                    first[ch_s] += 1

            if ch_t:  # If character from t is not None
                if ch_t not in second:
                    second[ch_t] = 1
                else:
                    second[ch_t] += 1

        return first == second
        
