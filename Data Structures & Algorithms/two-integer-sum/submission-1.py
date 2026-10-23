class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j=0
        k=1
        while j<len(nums) and k<len(nums):
            for i in range(k,len(nums)):
                if nums[j]+nums[i]==target:
                    return[j,i]
            j+=1
            k+=1
        
