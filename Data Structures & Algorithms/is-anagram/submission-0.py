class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t) and set(s)==set(t):
            return True
        return False
        