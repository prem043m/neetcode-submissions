class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}") # [3#cat,4#pack]
        return "".join(result) # into a string 3#cat4#pack....
    def decode(self, s: str) -> List[str]:
            res = []
            i = 0
            while i < len(s):
                j = i
                # get to the '#' value before # value and i is lenght of word
                while s[j] != '#':
                    j += 1
                length = int(s[i:j])

                start_str = j+1
                end_str = start_str + length

                res.append(s[start_str:end_str])

                i = end_str
            return res


