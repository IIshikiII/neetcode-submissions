class TimeMap:

    def __init__(self):
        self.vals = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.vals.keys():
            self.vals[key].append((timestamp, value))
        else:
            self.vals[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        vals = self.vals.get(key, "")
        if vals == "":
            return ""
        if vals[0][0] > timestamp:
            return ""
        Lprev = 0
        L = 0
        R = len(vals) - 1
        while L <= R:
            mid = (L + R) // 2
            if vals[mid][0] < timestamp:
                L = mid + 1
            elif vals[mid][0] > timestamp:
                R = mid - 1
            else:
                return vals[mid][1]
        if vals[mid][0] < timestamp:
            return vals[mid][1]
        elif vals[mid][0] > timestamp:
            return vals[mid-1][1]

        
