class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check - if lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
            
        # Using an array of size 26 (constant space) for lowercase English letters
        # This gives us O(1) space complexity since the array size is fixed
        char_count = [0] * 26
        
        # Count characters in s
        for char in s:
            char_count[ord(char) - ord('a')] += 1
            
        # Decrement counts for characters in t
        for char in t:
            char_count[ord(char) - ord('a')] -= 1
            
        # If all counts are 0, strings are anagrams
        for count in char_count:
            if count != 0:
                return False
                
        return True