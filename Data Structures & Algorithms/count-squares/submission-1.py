class CountSquares:

    def __init__(self):
       self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        x,y  = point
        total = 0

        for (px,py),count_p in list(self.points.items()):
            if abs(px-x) != abs(py-y):
                continue
            if px== x or py==y:
                continue
                
            total+= count_p * self.points[(x,py)]* self.points[(px,y)]
        return total