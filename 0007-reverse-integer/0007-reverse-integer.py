class Solution:
    def reverse(self, x: int) -> int:
        arr = 0
        if x < 0:
            arr = int(str(x)[1:][::-1]) *-1
        else:
            arr = int(str(x)[::-1])
        if arr > 2 ** 31 - 1 or arr < -2**31:
            return 0
        return arr      
        