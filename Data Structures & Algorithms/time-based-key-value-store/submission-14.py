class TimeMap:

    def __init__(self):
        #initialise the hashmap for storing the key value pairs 
        from collections import defaultdict 
        self.data = defaultdict(list)



    def set(self, key: str, value: str, timestamp: int) -> None:
        #store the value in the form of tuple (t , v)
        self.data[key].append((timestamp, value))
        return None
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.data[key]:
            return ""
        #the idea is to be able to retrieve a value at any timestamp even tho the current timestamp is much in the future
        #perform binary search on the target timestamp with a max bound of <= timestamp
        #trying to be as large as possible but not exceeding
        l , r = 0 , len(self.data[key])-1
        res = ""
        while l <= r:
            mid = (r-l)//2 + l

            item =  self.data[key][mid]
            if item[0] <= timestamp:
                res = item[1]
                l = mid + 1
            else:
                r = mid-1 

        return res


