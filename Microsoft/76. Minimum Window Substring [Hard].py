class Solution:
    def minWindow(self, s: str, t: str) -> str:

        sDict = {}
        tDict = {}

        for char in t:
            tDict[char] = tDict.get(char, 0) + 1

        have = 0
        need = len(tDict)

        res = [0,0]
        resLength = float('inf')
        l = 0

        
        for r in range(len(s)):

            sDict[s[r]] = sDict.get(s[r], 0) + 1

            if(s[r] in tDict and sDict[s[r]]==tDict[s[r]]):
                have+=1
            
            while(have == need):

                if(r-l+1 < resLength):
                    resLength = r-l+1
                    res = [l, r]


                if(s[l] in tDict):

                    sDict[s[l]]-=1
                    
                    if(sDict[s[l]] < tDict[s[l]]):
                        have-=1
                
                l+=1

        l, r = res

        if(resLength != float('inf')):
            return s[l:r+1]
        else:
            return ""



        
        