class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        wind_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i],0)+1
            wind_count[s2[i]] = wind_count.get(s2[i],0)+1

        if s1_count == wind_count :
            return True
        
        for j in range(len(s1),len(s2)):
            new_char = s2[j]
            wind_count[new_char] = wind_count.get(new_char,0)+1

            left_char = s2[j-len(s1)]
            wind_count[left_char] -= 1

            if wind_count[left_char] == 0:
                del wind_count[left_char]
            
            if s1_count == wind_count:
                return True
        return False

