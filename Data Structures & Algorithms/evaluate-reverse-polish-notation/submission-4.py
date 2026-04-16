class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        # result = 0
        for char in tokens:
            if char in {"+", "-", "*", '/'}:
                num1 = nums.pop()
                num2 = nums.pop()
                print(num2, num1)
                if char == "+":
                    result = num2 + num1
                elif char == "-":
                    result = num2 - num1
                elif char == "*":
                    result = num2 * num1
                else:
                    result = int(num2 / num1)
                print(result)
                nums.append(result)
            else:
                nums.append(int(char))
        return nums.pop()