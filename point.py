# class Point


class Point:
    count_of_instance = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count_of_instance += 1

    def __del__(self):
        Point.count_of_instance -= 1

    def __repr__(self):
        return "Point(x={0}, y={1})".format(self.x, self.y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def show(self):
        print("[%d,%d]점을 그렸습니다." % (self.x, self.y))
        # print("{0},{1}점을 그렸습니다.".format(self.x, self.y))

    @staticmethod
    def static_method():
        print("static_method() called")

    @classmethod
    def class_method(cls):
        print("인스탄스 갯수: {0}".format(cls.count_of_instance))
        # print("class_method() called")
