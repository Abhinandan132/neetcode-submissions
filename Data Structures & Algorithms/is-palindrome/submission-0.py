class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() 
        text = [char for char in s if char.isalnum()] 
        l, h = 0, len(text) - 1
        while(l < h): 
            if (text[l] != text[h]): return False 
            l += 1
            h -=1 
        return True