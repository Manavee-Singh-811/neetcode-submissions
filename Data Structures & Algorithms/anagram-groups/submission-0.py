from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = {}
        
        for word in strs:
            key = tuple(sorted(Counter(word)))

            if key not in dictionary:
                dictionary[key] = []

            dictionary[key].append(word)
    
        return list(dictionary.values())
        


        