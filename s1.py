class Solution:
    def reverseWords(self,s:str) ->str:
        #pythonic
        return " ".join([word for word in reversed(s.split()) if word])
