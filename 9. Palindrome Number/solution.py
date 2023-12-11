class Solution(object):
    def isPalindrome(self, x: int ) -> bool :
        """
        :type x: int
        :rtype: bool
        """
        # Converting the integer to string and then to a list
        # to use the builtin .reverse() method
        # list_x = list(str(x))
        # reverse_list_x = list_x.copy()
        # reverse_list_x.reverse()
        # return reverse_list_x == list_x
        
        # without converting the integer to string
        if x < 0:
            return False

        reverse_x: int = 0
        temp: int = x
        
        while (temp != 0):
            digit = temp % 10
            reverse_x = reverse_x * 10 + digit
            temp = temp // 10

        return reverse_x == x