class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [''] * n
        
        ch = ord('a')
        
        # Step 1: Construct string
        for i in range(n):
            if res[i] == '':
                if ch > ord('z'):
                    return ""
                res[i] = chr(ch)
                
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        res[j] = res[i]
                
                ch += 1
        
        s = ''.join(res)
        
        # Step 2: Validate
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return s
        