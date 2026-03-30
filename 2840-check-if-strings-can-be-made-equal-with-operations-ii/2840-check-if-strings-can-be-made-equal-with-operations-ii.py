class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_s1 = Counter()
        odd_s1 = Counter()
        even_s2 = Counter()
        odd_s2 = Counter()
        
        for i in range(len(s1)):
            if i % 2 == 0:
                even_s1[s1[i]] += 1
                even_s2[s2[i]] += 1
            else:
                odd_s1[s1[i]] += 1
                odd_s2[s2[i]] += 1
        
        return even_s1 == even_s2 and odd_s1 == odd_s2
        