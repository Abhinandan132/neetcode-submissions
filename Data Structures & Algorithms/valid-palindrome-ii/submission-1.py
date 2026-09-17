class Solution:
    def isPalindrome(self, s, l, h): 
        while(l < h): 
            if (s[l] != s[h]): 
                return False 
            l += 1
            h -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        s = s.lower() 
        text = [char for char in s if char.isalnum()] 
        l, h = 0, len(text) - 1
        while(l < h): 
            if (text[l] != text[h]): 
                # Check whether we can skip characters from either. 
                return (self.isPalindrome(s, l + 1, h) or self.isPalindrome(s, l, h - 1))
            l += 1
            h -= 1
        return True
