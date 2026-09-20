class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = [] 
        for o in operations: 
            if (o == '+'): 
                records.append(records[-1] + records[-2]) 
            elif (o == 'D'): 
                records.append(2 * records[-1]) 
            elif (o == 'C'): 
                records.pop() 
            else: records.append(int(o))
        return sum(records)