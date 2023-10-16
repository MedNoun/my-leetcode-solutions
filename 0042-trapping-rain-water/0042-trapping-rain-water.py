class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        max_i = height[i]
        j = len(height) - 1
        max_j = height[j]
        s = 0
        while i<j:
            if max_i <= max_j:
                addition = max_i - height[i]
                i+=1
                max_i = max(max_i, height[i])
            else:
                addition = max_j - height[j]
                j-=1
                max_j = max(max_j, height[j])
            if addition > 0:
                s+=addition
           
        return s


            