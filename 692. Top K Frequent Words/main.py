from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or len(words) < 1:
            return None
        
        frecuencies = {}

        for word in words:
            if word in frecuencies:
                frecuencies[word] += 1
            else:
                frecuencies[word] = 1

        group = [(k,v) for k, v in frecuencies.items()]
        group.sort(key=lambda x: (-x[1], x[0]))

        words = []
        for i in range(k):
            words.append(group.pop(0)[0])

        return words
    
s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)) # ["i", "love"]
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)) # ["the", "is", "sunny", "day"]
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3)) # ["i", "love", "coding"]
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1)) # ["i"]
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 0)) # []
