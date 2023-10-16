class Solution:
    def trap(self, height: List[int]) -> int:
        r_max = []
        l_max = []
        ri_max = 0
        li_max = 0
        for i in range(len(height)):
            li_max = max(li_max,height[i])
            l_max.append(li_max)
            ri_max = max(ri_max,height[-i-1])
            r_max = [ri_max] + r_max
        result = 0
        
        for i in range(len(l_max)):
            result += min(l_max[i],r_max[i]) - height[i]
        return result
            