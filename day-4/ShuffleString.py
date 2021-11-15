def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        fin=list(range(len(s)))
        for num,ele in enumerate(indices):
            fin[ele]=s[num]
        return "".join(fin)
        
        