class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

            
        res = []
        self.dfs(n,n,[],res,n)
        return res
    def dfs(self, left, right, path, res, n):
        if right < left or left < 0 or right < 0:
            return
        if len(path) == 2*n:
            res.append("".join(path))
        self.dfs(left-1, right, path+['('], res, n)
        self.dfs(left, right-1, path+[')'],res,n)