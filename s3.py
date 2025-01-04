class Solution:
    def reverseWords(self,s:str) ->str:
        ret=[]
        for i,char in enumerate(s):
            last_char=s[i-1] if i!=0 else None
            if char == last_char and char==" ":
                continue
            else:
                ret.append(char)
        ret="".join(ret)
        return  " ".join(ret.split(" ")[::-1]).strip()
