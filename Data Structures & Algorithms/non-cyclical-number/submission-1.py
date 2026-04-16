class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        setnum = {number}
        while True:
            parser = [int(i) for i in list(str(number))]
            sumx = sum([x**2 for x in parser])
            if sumx == 1:
                return True
            if sumx in setnum:
                # print(sumx)
                return False
            setnum.add(sumx)
            number = sumx
