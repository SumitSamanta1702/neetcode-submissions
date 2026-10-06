class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]]+=1
            else:
                seen[nums[i]]=1
            
        list1=[]
        result=[]
        for key,value in seen.items(): 
            list1.append([value,key])
        list1.sort(reverse=True)
        for i in range(k):
            result.append(list1[i][1])
        return result 



