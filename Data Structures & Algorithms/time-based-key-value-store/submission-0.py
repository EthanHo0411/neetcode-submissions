class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])
        return None
    def get(self, key: str, timestamp: int) -> str:
        #binary search to find the correct timestamp and then return the value
        l , r = 0 , len(self.store[key])-1
        result = ""
        while l <= r:
            mid = l + ((r-l)//2)
            value = self.store[key][mid]
            if value[1] == timestamp:
                return value[0]
            elif value[1] > timestamp:
                r = mid-1
            else:
                l = mid+1
                result = value[0]
        return result
