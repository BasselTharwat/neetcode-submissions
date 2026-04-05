class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        startIndex = 0
        lastIndex = 1

        if s.isspace():
            return 1

        if len(s) == 1:
            return 1


        curr = s[startIndex:lastIndex]

        while lastIndex < len(s):
            lastIndex += 1

            if s[lastIndex-1] in curr:
                startIndex += 1
                lastIndex -= 1
            
            curr = s[startIndex:lastIndex]

            longest = len(curr) if len(curr) > longest else longest
            
        
        return longest
        