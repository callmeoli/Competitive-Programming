class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        n = len(s)
        res = []
        dic = {}
        
        for word in words:
            dic[int(word[-1])] = word[:-1]
        for i in sorted(dic.keys()):
            res.append(dic[i])        
        return " ".join(res)
