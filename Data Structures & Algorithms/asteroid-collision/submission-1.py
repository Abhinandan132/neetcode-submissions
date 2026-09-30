class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = [] 
        for a in asteroids: 
            while(st and st[-1] > 0 and a < 0): 
                impact = st[-1] + a 
                if (impact < 0): 
                    st.pop() 
                elif (impact > 0): 
                    a = 0 
                else: 
                    a = 0 
                    st.pop()
            if (a): st.append(a) 
        return st 
             