class Solution:
    def countArrangement(self, n: int) -> int:
        def DFS(status, idx, cnt):
            if idx > n:
                cnt+=1
                return cnt
            for i in range(1,n+1):
                if (not status[i-1] and (i % idx ==0 or idx % i ==0)):
                    status[i-1] = True
                    cnt = DFS(status, idx+1, cnt)
                    status[i-1] = False
            return cnt
        status = [False]*n
        idx, cnt = 1, 0
        return DFS(status, idx, cnt)