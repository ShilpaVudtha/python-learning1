class Point():
    def __init__(self, x = 0,y = 0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x +=x
        self.y +=y    

    def _add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def _sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def _mul__(self, p):
        return self.x * p.x, self.y * p.y


p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p2*p3

print(p5,p6,p7)