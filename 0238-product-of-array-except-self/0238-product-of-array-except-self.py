class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]
        post = [1]
        final = []
        for i in range(1,len(nums)):
            pre.append(pre[-1] * nums[i-1])
            post.append(post[-1] * nums[-i])
        for i in range(len(nums)):
            final.append(pre[i]*post[-i-1])
        return final       