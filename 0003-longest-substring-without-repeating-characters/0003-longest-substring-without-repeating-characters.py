class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            # If the character is already in the window, move the start
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            # Update the character's index
            char_index[char] = end
            
            # Calculate the maximum length
            max_length = max(max_length, end - start + 1)
        
        return max_length