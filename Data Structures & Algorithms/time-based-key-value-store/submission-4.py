class TimeMap:

    def __init__(self):
        self.dic = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [[timestamp, value]]
        else:
            self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.dic.keys():
            return result
        else:
            records = self.dic[key]
            l, r = 0, len(records)-1
            while l <= r:
                m = (l + r) // 2
                ts, tv = records[m]
                if ts <= timestamp:
                    result = tv
                    l = m + 1
                else:
                    r = m - 1
            return result