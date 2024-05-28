class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize variables
        current_string = ''
        max_length = 0
        
        # Iterate through the string
        for i in range(len(s)):
            # Check if the character is in current_string
            if s[i] in current_string:
                # Find the index of the first occurrence of the character in current_string
                start_index = current_string.find(s[i])
                # Update current_string to exclude the part before the first occurrence
                current_string = current_string[start_index + 1:] + s[i]
            else:
                # Add the character to current_string
                current_string += s[i]
            
            # Update max_length if current_string is longer
            max_length = max(max_length, len(current_string))
        
        return max_length

        