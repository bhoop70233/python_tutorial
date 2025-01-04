class Solution:
    def reverseWords(self,s:str) ->str:
        size=len(s)

        sArr=[]
        left=0
        right=0

        while right<size:
            if s[left]==' ':
                left+=1
                right+=1
            elif s[right]==' ':
                sArr.append(s[left:right])
                right+=1
                left=right

            else:
                right +=1
        if left !=right:
            sArr.append(s[left:right])

        return " ".join(sArr[::-1])
