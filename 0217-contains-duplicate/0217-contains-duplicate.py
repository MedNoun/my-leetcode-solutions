class Solution:
    def mergeSort(self,arr):
        if(len(arr)>1):
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            s_left = self.mergeSort(left)
            s_right = self.mergeSort(right)
            i =0
            j =0
            counter = 0
            while(i<len(s_left) and j<len(s_right)):
                if(s_left[i]<s_right[j]):
                    arr[counter] = s_left[i]
                    i+=1
                else:
                    arr[counter] = s_right[j]
                    j+=1
                counter+=1

            while(i<len(s_left)):
                arr[counter] = s_left[i]
                i+=1
                counter+=1

            while(j<len(s_right)):
                arr[counter] = s_right[j]
                j+=1
                counter+=1
                
        return arr
    
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        sort = self.mergeSort(nums)
        for i in range(length - 1) :
            if(nums[i] == nums[i+1]):
                return True
            
        return False
            
        