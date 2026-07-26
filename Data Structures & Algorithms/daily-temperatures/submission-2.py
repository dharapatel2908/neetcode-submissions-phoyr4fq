class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use stack and in stack add value and temp together
        # compare value if the value with the stack[-1] and current pointer 
        # if the value of stack[-1] is greater add back in the stack or else add current pointer in the stack
        # return the result list
        stack = []
        result = [0]*len(temperatures)
        for index,val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stacktemp, stackindex= stack.pop()
                result[stackindex] = index - stackindex
            stack.append((val,index))
        return result