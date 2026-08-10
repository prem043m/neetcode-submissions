class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1 without sort O(n*m)
        anagram_map = defaultdict(list)
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-ord('a')] += 1
            
            key = tuple(count)
            anagram_map[key].append(s)
        return list(anagram_map.values())

        # 2 using sort and dictionary with default values O(n*mlong(m))

        # res = defaultdict(list)
        # for s in strs:
        #     res["".join(sorted(s))].append(s)
        # return list(res.values())
