class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,j in enumerate(nums):
            comp=target-j
            if comp in dic:
                return[dic[comp],i]
            else:
                dic[j]=i


        
