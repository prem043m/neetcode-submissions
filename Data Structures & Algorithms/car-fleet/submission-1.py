class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        # stack = []
        fleet = 0
        max_time = 0
        for p,s in cars:
            time = (target-p)/s

            if time > max_time:
                max_time = time
                fleet += 1
            # if not stack or (time > stack[-1]):
            #     stack.append(time)
        # return len(stack)
        return fleet