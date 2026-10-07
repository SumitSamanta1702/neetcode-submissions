class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            res=res+str(len(word))+'#'+word
        return res
      
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            word_len=int(s[i:j])
            cut=s[j+1:j+1+word_len]
            res.append(cut)
            i=j+1+word_len
        return res

    
        