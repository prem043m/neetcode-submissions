class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st = 0
        end = len(numbers)-1
        while(st <= end):
            sum = numbers[st] + numbers[end]
            if sum < target :
                st += 1
            elif sum > target :
                end -= 1
            else:
                return [st+1,end+1]
        return [-1,-1]
