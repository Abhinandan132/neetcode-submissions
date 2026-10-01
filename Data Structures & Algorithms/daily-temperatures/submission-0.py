class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Naive Approach: O(n^2), O(n) SC. 
        n = len(temperatures) 
        st = []
        res = [0] * n 
        for i, t in enumerate(temperatures): 
            while(st and t > st[-1][0]): 
                st_temp, st_ind = st.pop() 
                res[st_ind] = i - st_ind
            st.append((t, i))
        return res 