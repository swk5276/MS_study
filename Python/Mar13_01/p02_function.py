# 함수
# 언제 ? : 소스 정리하여 계속 사용하기 위해서

# lambda함수 : 무명의 1회용 함수
# 언제 ? [괄호는 옵션]
(lambda x:print("김성웅"*x))(3)
#=>함수로 변환하면?
def name1(x):
    print("김성웅"*x)
name1(3)


def name(name):
    return print(name)
name("김성웅")

# 숫자 2개 넣으면 합 함수
c = (lambda a,b: a+b)(2,4)
print(c)
# 람다 함수를 일반 함수로 바꾸면?
def num_plus(a,b):
    c = a+b
    return print(c)
num_plus(5,7)



