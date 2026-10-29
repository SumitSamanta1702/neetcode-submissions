class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        l=[]
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        sorted_keys=sorted(dic.keys(),key=dic.get,reverse=True)
        
        return sorted_keys[0:k] 

        
        
        

        
        