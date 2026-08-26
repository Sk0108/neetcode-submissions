class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0] * len(temperatures)
        stack=[]
        for temp in range(len(temperatures)):
            while stack and temperatures[temp]> temperatures[stack[-1]]:
                prev_index= stack.pop()
                result[prev_index]= temp- prev_index
            stack.append(temp)
        return result


