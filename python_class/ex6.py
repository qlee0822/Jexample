#스테틱, 클래스, 인스턴스 메소드 모두 클레스 안에서 정의

#인스턴스 메소드 인스턴스를 통해 호출 self를 첫 번째 인자로 사용
#클래스 메소드 클래스를 통해 보출 @classmethod 정의, cls를 첫번째 인자로 사용

#스태틱 메소드는 첫번째 인자를 받지 않는다
#스태틱 메소드는 클래스와 연광성이 있는 함수를 클래스 안에 정의하여 클래스나 인스턴스를 통해서 호출
# @staticmethod 데코레이터를 사용하여 정의

class Demon:
    num = 0
    @staticmethod
    def add(x, y):
        # return x+y
        return x + y + Demon.num

d = Demon()
print(d.add(10, 20))

print(Demon.add(30,40))