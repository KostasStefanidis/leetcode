class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while s[-1] == ' ':
            s = s.removesuffix(' ')
        
        word = s.split(' ')
        return len(word[-1])