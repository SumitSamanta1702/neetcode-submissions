class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen={}
        for i in range(len(strs)):
            word=strs[i]
            sorted_word="".join(sorted(word))
            if sorted_word not in seen:
                seen[sorted_word]=[]
            seen[sorted_word].append(word)
        return list(seen.values())
    
