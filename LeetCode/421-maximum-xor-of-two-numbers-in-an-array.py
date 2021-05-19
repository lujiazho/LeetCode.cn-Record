###############################################################################################
# 借鉴官方方法，有一点贪心算法的思想，对x从高位到低位的顺序，最好的情况是最后得到的x每一位都为1就最大
# 因此遍历时假设该位为1，利用异或的性质，该x(前k位)乘上每一个数组中的数(同样取前k位)所得到的数，
# 如果该x在第k位可以为1，则所得到的数一定在哈希表中
###########
# 时间复杂度：O(nlogC)，n为数组长度，C为数组元素大小的范围，本题中C＜2^31，logC大概为32，哈希表查找时间忽略不计(按官方的意思)
# 空间复杂度：O(n)，哈希表的空间
###############################################################################################
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 从最高位开始，其二进制位编号为 30
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            # 将所有的 pre^k(a_j) 放入哈希表中
            for num in nums:
                seen.add(num >> k)

            # 假设x的新一位为1是可以的（这也是我们希望的，为了尽可能使x的每一位都为1）
            x_next = x * 2 + 1
            found = False
            
            # 枚举这个x和每个数的结果，如果在哈希表里，说明这个x是可以的
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found: # 则表示可以为1
                x = x_next
            else:
                # 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
                # 则要减回去
                x = x_next - 1
        
        return x