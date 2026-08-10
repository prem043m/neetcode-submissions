class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        #1 
        if len(s) != len(t):
            return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        return all(x == 0 for x in count)
        #2 
        #return Counter(s) == Counter(t)
        
        #3
        # if len(s) != len(t):
        #     return False
        # countS , countT  = {},{}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i],0) # get(key,default)
        #     countT[t[i]] = 1 + countT.get(t[i],0) 
        # return countS == countT