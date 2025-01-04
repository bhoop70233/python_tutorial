class Solution:
    def reverseWords(self,s:str)->str:

        left=0
        right=len(s)-1

        #Remove leading spaces
        while left <=right and s[left] ==' ':
            left +=1

        #Remove trailing spaces
        while right >=left and s[right] ==' ':
            right -=1
        #Step 2 :Extract words manually
        words=[]
        current_word=[]

        for i in range(left,right+1):
            if s[i] !=' ':
                current_word.append(s[i])
            else:
                if current_word: # End of a word
                    words.append(''.join(current_word))
                    current_word=[]
            # If the last word has not been added
            if current_word:
                words.append(''.join(current_word))

            # Step 3: Reverse the list of words manually
            left=0
            right =len(words) -1
            while left <right:
                words[left],words[right] = words[right],words[left]
                left +=1
                right -=1
            #Step 4: MAnually join words with a single space
            result=''
            for word in words:
                result+=word + ' '

            # Remove the trailing space
            return result.strip()
