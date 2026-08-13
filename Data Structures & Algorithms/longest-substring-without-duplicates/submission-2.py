class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        l,r = 0,1
        max = 1
        while r < len(s):
            if l == r:
                r += 1
                continue
            if s[l] not in seen:
                seen.add(s[l])
                continue
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1
                max = len(seen) if max < len(seen) else max

        return max