class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqMap_s = {}
        freqMap_t = {}
        for i in range(len(s)):
            freqMap_s[s[i]] = 1 + freqMap_s.get(s[i],0)
            freqMap_t[t[i]] = 1 + freqMap_t.get(t[i],0)
        
        return freqMap_s == freqMap_t
