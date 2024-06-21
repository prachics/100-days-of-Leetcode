class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)
        
        for i in nums:
            m[i]+=1
        
        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0

         

