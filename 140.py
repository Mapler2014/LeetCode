
def wordBreak(s, wordDict) :
    N = len(s)
    #@lru_cache(None)
    def DP(index):
        if index == N:
            return [[]]
        solution = []
        for i in range(index, N):
            word = s[index:i+1]
            if word not in wordDict:
                continue
            for value in DP(i+1):
                solution.append([word]+value)
        return solution
    return [" ".join(i) for i in DP(0)]

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s=wordBreak(s,wordDict)
print(s)