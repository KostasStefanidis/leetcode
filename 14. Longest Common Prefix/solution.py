class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # 1 <= strs.length <= 200
        # 0 <= strs[i].length <= 200
        # strs[i] consists of only lowercase English letters.
        
        smallest_word = min(strs, key=len)
        i = 0
        common_prefix = ''
        
        is_common_letter = True
        while(i < len(smallest_word) and is_common_letter):
            for string in strs:
                if string == smallest_word:
                    continue
                
                if smallest_word[i] != string[i]:
                    is_common_letter = False
                    break
            
            if is_common_letter:
                common_prefix += smallest_word[i]
        
            i = i + 1
        
        return common_prefix