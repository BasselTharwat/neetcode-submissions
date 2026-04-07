class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for i in range(k):
            max_key = max(freq, key=freq.get)
            print("freq now: ", freq)
            print("max now: ", max_key)
            result.append(max_key)
            del freq[max_key]

        return result


        