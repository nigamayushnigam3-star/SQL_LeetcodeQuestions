class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        i = len(s) - 1

        # Ignore spaces at the end
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count last word
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count
        