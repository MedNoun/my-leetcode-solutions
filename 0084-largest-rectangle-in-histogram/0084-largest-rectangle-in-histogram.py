class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                result = max(result, (i - index)*height)
            stack.append((index,h))
        while stack:
            index, height = stack.pop()
            result = max(result, height*(len(heights) - index))
        return result             