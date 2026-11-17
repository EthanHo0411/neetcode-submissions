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
            #if the timestamp excatly equal the current one, return early
            if value[1] == timestamp:
                return value[0]
            
            #if the mid is larger than the current timestamp, go to lower timestamps
            elif value[1] > timestamp:
                r = mid-1
            #if the mid is smaller than the current timestamp, go to higher timestamps
            #the result variable keep track of the biggest timestamp that is possible
            # the variable is used because l would probably point to a value larger than the timestamp at the end
            else:
                l = mid+1
                result = value[0]
        return result
