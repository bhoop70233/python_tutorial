class Solution:
    def reverseWords(self,s:str)->str:

        if len(s)==0 or len(s)==1:
            return s
        words=s.split(" ")
        arr =[]
        for word in words:
            if word.strip() =='':
                continue
            else:
                arr.append(word.strip())
        print(arr)
        for i in range(0,len(arr)//2):
            index1=i
            index2=-(i+1)
            temp=arr[index1]
            arr[index1]=arr[index2]
            arr[index2]=temp

        return " ".join(arr)
