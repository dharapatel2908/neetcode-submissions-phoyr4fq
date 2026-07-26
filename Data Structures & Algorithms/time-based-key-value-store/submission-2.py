class TimeMap:

    def __init__(self):
        self.store ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((int(timestamp), value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        items = self.store[key]
        left = 0
        right = len(items)-1
        result = ""

        while left <= right:
            mid = (left+right)//2
            if items[mid][0] <= timestamp:
                result = items[mid][1]
                left = mid+1
            else:
                right = mid-1
        
        return result