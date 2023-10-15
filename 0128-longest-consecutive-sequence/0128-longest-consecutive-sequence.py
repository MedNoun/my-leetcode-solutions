class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0
        
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_seq = 1
                while current_num+1 in num_set:
                    current_num += 1
                    current_seq += 1
                longest_seq = max(longest_seq, current_seq)
                
        return longest_seq