class Solution:
    def isValid(self, s: str) -> bool:
        st = [] 
        close_open_pair = {')':'(', '}':'{',']':'['} 
        for c in s: 
            if c in close_open_pair: # Is a closing bracket. 
                if st and st[-1] == close_open_pair[c]: 
                    st.pop() 
                else: return False 
            else: st.append(c) # Is a opening bracket. 
        return True if not st else False