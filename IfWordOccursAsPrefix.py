# PROBLEM: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/

1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        ans = list(sentence.split())
        count = 0
        
        for word in ans:
            count += 1
            if word.startswith(searchWord):
                return count

        return -1
