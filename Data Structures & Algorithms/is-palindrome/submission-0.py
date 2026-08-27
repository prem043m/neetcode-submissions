class Solution:
    def isalnum(self,ch):
        if (ch >= '0' and ch <= '9') or (ch >= 'a' and ch <= 'z'):
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        lowerd = s.lower()
        st = 0
        end = len(s)-1
        while(st <= end):
            if not self.isalnum(lowerd[st]):
                st += 1
            elif not self.isalnum(lowerd[end]):
                end -= 1
            else:
                if lowerd[st] != lowerd[end]:
                    return False
                st += 1
                end -= 1
        return True