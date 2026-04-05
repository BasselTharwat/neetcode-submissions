class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 1:
            return 0
            
        left = 0
        right = 1
        longest = 1
        current_longest = 1
        

        for left in range(len(s)):
            if current_longest > longest:
                longest = current_longest
            char_set = set()
            char_set.add(s[left])
            current_longest = 1
            right = left + 1
            while right < len(s) and s[right] not in char_set:
                char_set.add(s[right])            
                current_longest += 1
                right += 1
            
            
        return longest


        
        