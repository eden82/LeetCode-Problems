class Solution:
    def isPalindrome(self, x: int) -> bool:
        To_String = str(x)
        reversed_int = To_String[::-1]
        if reversed_int == To_String :
            return True
        else:
            return False