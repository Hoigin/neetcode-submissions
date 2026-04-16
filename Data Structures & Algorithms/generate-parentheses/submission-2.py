class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        # 将左、右括号的数量直接作为参数传入
        def backtrack(path, left_count, right_count):
            # 终止条件：当路径长度达到 2*n 时，说明找到了一个合法组合
            if len(path) == 2 * n:
                res.append(path)
                return
            
            # 选择 1：只要左括号没用完，就可以一直加左括号
            if left_count < n:
                backtrack(path + '(', left_count + 1, right_count)
                
            # 选择 2：只有当右括号的数量小于左括号时，加右括号才是合法的
            if right_count < left_count:
                backtrack(path + ')', left_count, right_count + 1)
                
        # 初始状态：空字符串，左右括号数量均为 0
        backtrack("", 0, 0)
        return res