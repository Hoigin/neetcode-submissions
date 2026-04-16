class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        setnum = {number}
        while True:
            sumx = sum([int(i)**2 for i in list(str(number))])
            if sumx == 1:
                return True
            if sumx in setnum:
                return False
            setnum.add(sumx)
            number = sumx
