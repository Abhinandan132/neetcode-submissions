class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2) 
        i, j, s = 0, 0, ""
        while(i < n1 and j < n2): 
            s += word1[i]
            i += 1
            s += word2[j]
            j += 1
        while(i < n1): 
            s += word1[i]; i += 1
        while(j < n2): 
            s += word2[j]; j += 1
        return s