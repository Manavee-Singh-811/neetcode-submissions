from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(list(s))==Counter(list(t)):
            return True
        return False
        