class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        ar = self.store.get(key, None)
        if not ar: self.store[key] = [(timestamp, value)]
        else: self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        ar = self.store.get(key, None)
        if not ar : return ""
        l, r = 0, len(ar) - 1
        while l<=r:
            m =(l+r)//2
            if ar[m][0]>timestamp:
                r = m-1
            elif ar[m][0]<timestamp:
                l = m+1
            else:
                return ar[m][1]
        if ar[r][0] < timestamp : 
            return ar[r][1] 
        else : 
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)