# class MyStr


class MyStr:

    def __init__(self, s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        return self.s + other

    def __radd__(self, other):
        return other + self.s

    def __mul__(self, other):
        return MyStr(self.s * other)

    def __neg__(self):
        return self.s[::-1]

    def __str__(self):
        return self.s


s = MyStr('Hello Python')
t = s / ' '
print(t)

print(s + ' ~~~')

print(MyStr('python')*3)

print('hello' + ' ' + MyStr('world'))

print(-MyStr('python'))