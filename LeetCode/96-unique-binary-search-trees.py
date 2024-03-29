###############################################################################################
# 01背包问题的思想 + 记忆化搜索dp + 暴搜，但超时
###########
# 时间复杂度：O(2^(2^n))，n个数，最多可n层，所有节点共2^n个，每个都有选或不选两种，此题n最大19, 所以2^(2^n) ≈ 计算器算出ERROR
# 空间复杂度：O(2^n)
###############################################################################################
class Solution:
    def numTrees(self, n: int) -> int:
        N = 2**n
        res, dp = 0, [0]*N
        def dfs(i, u):
            nonlocal res
            if u == n:
                res += 1
                return
            if i == N:
                return
            if i == 1 or dp[i//2] == 1:
                dp[i] = 1
                dfs(i+1, u+1)
            dp[i] = 0
            dfs(i+1, u)
            
        dfs(1, 0)
        return res

###############################################################################################
# 基本思路：以某个点为根节点，其左右子树节点树不同，则得到的结构一定不同
# 因此我们以不同点根节点进行遍历
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1) # G[i]表示长度为i的序列能组成不同二叉搜索树的个数
        G[0], G[1] = 1, 1 # 当长度为0和1时，只有一种

        for i in range(2, n+1): # 从小到大计算长度不同时的G值，有点dp的思想
            for j in range(1, i+1): # 以不同点为根节点
                G[i] += G[j-1] * G[i-j] # G[i] += 以某个点j为根，根左边j-1个，根右边i-j个，并且组合方案为笛卡尔积，因为左右子树的根有不同组合

        return G[n]