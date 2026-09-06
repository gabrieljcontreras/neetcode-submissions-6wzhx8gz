class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end
    
        while start <= end: 
            k = (end + start) // 2
            time = 0
            for p in piles: 
                time += (p + k - 1) // k
            
            if time <= h: 
                res = k
                end = k - 1
            else: 
                start = k + 1
        
        return res