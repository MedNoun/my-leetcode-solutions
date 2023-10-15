import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        h = {}
        l = {}
        ind = []
        for num in nums:
            higher = h.get(num - 1)
            lower = l.get(num + 1)
            if(higher != None):
                tup = ind[higher]
                new_tup = (tup[0],num)
                ind[higher] = new_tup
                del h[num - 1]
                h[num] = higher
            if(lower != None):
                tup = ind[lower]
                new_tup = (num,tup[1])
                ind[lower] = new_tup
                del l[num + 1]
                l[num] = lower
            if(higher == None and lower == None):
                h[num], l[num] = len(ind),len(ind)
                ind.append((num,num))
        i=0
        items = list(h.items())
        while(True):
            if i>=len(items):
                break
            high = items[i]
            high_value, high_index = high[0], high[1]
            low_index = l.get(high_value)
            if(high_index != low_index and low_index != None):
                new_low = ind[high_index][0]
                new_high = ind[low_index][1]
                new_index = len(ind)
                ind.append((new_low,new_high))
                del h[high_value]
                del l[high_value]
                h[new_high] = new_index
                l[new_low] = new_index
                items[i] = (new_high,new_index)
                i-=1
            else:
                i+=1
        maximum = 0
        for seq in ind:
            maximum = max(seq[1] - seq[0] + 1,maximum)
        return maximum




        