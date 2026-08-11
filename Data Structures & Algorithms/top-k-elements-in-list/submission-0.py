class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        bucket = [[] for _ in range(len(nums)+1)]
        # using bucket to for having similar count for other elements that avoid overwrite
        for num,count in freq.items():
            bucket[count].append(num)
        
        # for each element in bucket 
        result = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        