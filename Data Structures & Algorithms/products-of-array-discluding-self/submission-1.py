class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        output=[]
        mult=1
        for i in range(len(nums)):
            prefix.append(mult)
            mult=mult*nums[i]# I done this for shifting one element in the list
        mult=1
        for i in range(len(nums)-1,-1,-1):
            postfix.append(mult)
            mult=mult*nums[i]
        postfix.reverse()
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])
        return output
