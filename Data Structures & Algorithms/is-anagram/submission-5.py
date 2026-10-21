class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char]+=1
        tMap = {}
        for char in t:
            if char not in tMap:
                tMap[char] = 1
            else:
                tMap[char]+=1
            if char in tMap and char not in sMap:
                return False
        for char in t:
            if sMap[char] != tMap[char]:
                return False
        return True