from math import hypot
# hypot 메서드는 sqrt(x * x + y * y) -> x제곱 + y제곱의 루트값

class Vector:

    def __init__(self, x:int=0, y:int=0) -> None:        
        self.x = x
        self.y = y

    # 객체를 문자열로 표현
    def __repr__(self) -> str:
        return 'Vector(%r, %r)' % (self.x, self.y)  # %r은 __repr__에서 설정한 값
    
    def __abs__(self) -> int:
        return hypot(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar:int):
        return Vector(self.x * scalar, self.y * scalar)

    def __bool__(self):
        return bool(abs(self))
    
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# __repr__
print(v1, v2)
# __add__
print(v1 + v2)
# __abs__
print(abs(v1), abs(v2))
# __mul__
print(v1 * 3)
# __bool__
print(bool(v1))

print('------'*10)

# 만약 인수로 문자열을 입력하면?
v3 = Vector('3', '4')
print(v3)
# print(v1 + v3)
# print(abs(v3))