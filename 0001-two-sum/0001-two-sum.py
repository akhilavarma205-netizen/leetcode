class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for a in range(0,n):
            num=nums[a]
            b=target-num
            if(b in d):
                return[a,d[b]]
            d[num]=a