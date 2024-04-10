class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            new_num=int("".join(list(reversed(str(x)))))
            return new_num==x
        else:
            return False
        