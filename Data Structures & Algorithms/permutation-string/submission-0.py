class Solution:
    """
    lecaabee
      |
       |
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = {}
        for letter in s1:
            freq_s1[letter] = freq_s1.get(letter, 0) + 1

        freq_sub_s2 = {}
        for i in range(len(s1)):
            freq_sub_s2[s2[i]] = freq_sub_s2.get(s2[i], 0) + 1

        if freq_sub_s2 == freq_s1:
            return True

        j = 0
        k = len(s1)

        while k < len(s2):
            # remove left char
            freq_sub_s2[s2[j]] -= 1
            if freq_sub_s2[s2[j]] == 0:
                del freq_sub_s2[s2[j]]

            # add right char
            freq_sub_s2[s2[k]] = freq_sub_s2.get(s2[k], 0) + 1

            if freq_sub_s2 == freq_s1:
                return True

            j += 1
            k += 1

        return False       
    

    