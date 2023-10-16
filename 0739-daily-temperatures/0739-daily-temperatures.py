class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temp))]
        stack = []
        for curr_pos,curr_val in enumerate(temp):
            while stack and curr_val > stack[-1][1] :                    
                    top_pos,top_val = stack.pop()
                    ans[top_pos] = curr_pos-top_pos                
            stack.append((curr_pos,curr_val))            
        return ans

                
       