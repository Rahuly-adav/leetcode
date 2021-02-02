class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """dic="QWERTYUIOPLKJHGFDSAZXCVBNM"
        l=len(word)
        cap,small=0,0
        for i in range(l):
            if word[i] in dic:
                cap+=1
            else:
                small+=1
        if cap==l or small==l:
            return True
        elif cap==1 and word[0] in dic:
            return True
        else:
            return False"""
        if(len(word)==1):
            return True
        elif(word.isupper()):
            return True
        elif(word.islower()):
            return True
        elif(word[0].isupper() and word[1:].islower()):
            return True
        else:
            return False