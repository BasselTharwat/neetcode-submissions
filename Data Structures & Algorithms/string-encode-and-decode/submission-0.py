class Solution:

    def encode(self, strs: List[str]) -> str:
        output_string = ""
        for string in strs:
            output_string += str(len(string)) + "#" + string

        print(output_string)

        return output_string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res
