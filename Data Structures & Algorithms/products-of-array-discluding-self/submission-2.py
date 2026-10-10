class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        output=[1]*len(nums)
        mult=1
        for i in range(len(nums)):
            prefix[i]=mult
            mult=mult*nums[i]# I done this for shifting one element in the list
        mult=1
        for i in range(len(nums)-1,-1,-1):
            postfix[i]=mult
            mult=mult*nums[i]
        
        for i in range(len(nums)):
            output[i]=prefix[i]*postfix[i]
        return output
