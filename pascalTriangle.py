class Solution:
    def generate(self, numRows):
        ans = []
        for i in range(numRows):
            row = [1] * (i + 1)
            ans.append(row)
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j] + ans[i - 1][j - 1]
        return ans