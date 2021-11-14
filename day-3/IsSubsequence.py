def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sIdx, tIdx=0,0
        while sIdx<len(s) and tIdx<len(t):
            if s[sIdx]==t[tIdx]:
                sIdx+=1
            tIdx+=1
        return sIdx==len(s)
        