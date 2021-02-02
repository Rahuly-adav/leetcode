class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="abcdefghijklmnopqrstuvwxyz1234567890"
        b=""
        for i in range(len(s)):
            if s[i].lower() in a:
                b+=s[i].lower()
        #print(b,b[::-1])
        if b==b[::-1]:
            return True
        else:
            return False