# class Rect


class Rect:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return 'Rect(%d, %d, %d, %d)' % (self.x1, self.y1, self.x2, self.y2)

    def __repr__(self):
        return 'Rect(%d, %d, %d, %d)' % (self.x1, self.y1, self.x2, self.y2)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def area(self):
        return (self.x2-self.x1) * (self.y2-self.y1)

    def draw(self):
        print('Rect(%d, %d, %d, %d)를 그렸습니다' % (self.x1, self.y1, self.x2, self.y2))
