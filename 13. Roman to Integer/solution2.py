class Solution:
    def __init__(self):
        self.roman_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        sum: int = 0
        i: int = 0
        symbols = list(self.roman_mapping.keys())

        while (i < len(s)):
            current_char = s[i]
            num: int = self.roman_mapping.get(current_char)

            if i != len(s)-1:
                # if the character is not the last get the next one also
                next_char = s[i+1]

                if symbols.index(next_char) - symbols.index(current_char) == 1 or symbols.index(next_char) - symbols.index(current_char) == 2:
                    num = self.roman_mapping.get(next_char) - self.roman_mapping.get(current_char)
                    i = i + 1

            sum = sum + num
            i = i + 1

        return sum
