class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:  
        arr = [[p, s] for p, s in zip(position, speed)]
        arr.sort(key = lambda x: x[0], reverse = True) 
        st = [] 
        for pos, speed in arr: 
            st.append((target - pos)/speed)
            if (len(st) >= 2 and st[-1] <= st[-2]): 
                st.pop() # Gets caught up by. 
        return len(st)