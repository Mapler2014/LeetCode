'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]
 

Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n =len(S)
        solution = list()
        def dfs(path, index):
            if index == n:
                solution.append(path)
                return
            if S[index].isalpha():
                dfs(path+S[index].lower(), index+1)
                dfs(path+S[index].upper(),index+1)
            elif S[index].isdigit():
                dfs(path+S[index],index+1)
            else:
                print("Letters Or Digits Only")
            
        if n>=1 and n<=12:
            dfs("",0)
            return solution
        else:
            print("The length should be between 1 and 12")