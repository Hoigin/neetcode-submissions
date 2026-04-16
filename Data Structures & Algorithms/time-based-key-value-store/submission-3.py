class TimeMap:

    def __init__(self):
        self.dic = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.dic:
            return self.dic[(key, timestamp)]
        else:
            timestamps = [k2 for k1, k2 in self.dic.keys() if key==k1]
            if not timestamps:
                return ""
            else:
                l, r = 0, len(timestamps)-1
                result = ""
                while l <= r:
                    m = (l+r) // 2
                    if timestamps[m] < timestamp:
                        result = self.dic[(key, timestamps[m])]
                        l = m + 1
                    else:
                        r = m - 1
                return result
