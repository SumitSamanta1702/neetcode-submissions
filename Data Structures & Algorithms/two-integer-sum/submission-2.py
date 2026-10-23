class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j=0
        while j<len(nums):
            for i in range(j+1,len(nums)):
                if nums[j]+nums[i]==target:
                    return[j,i]
            j+=1
            
        
