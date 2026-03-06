class Solution:
    def reverseWords(self, s: str) -> str:
        #without using python functions
        words = []
        i , j = 0,0
        word = ""
        while j<len(s):
            if s[j].isalnum():
                word += s[j]
            else:
                if word!= "":
                    words.append(word)
                word = ""
                i = j
            if j == len(s)-1 and word != "":
                words.append(word)
            j+=1
        return " ".join(words[::-1])

        #using python functions
        words= s.split()
        return " ".join(words[::-1])
