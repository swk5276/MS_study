#PL의 function
# 연관된 작업을 묶어서 정의
# 필요 시 마다 사용

# 다른언어: main함수 영역
# 띄어쓰기 엔터 무의미
# python : interpreter 영역
# 들여쓰기

# 1) 정의
# def 함수명(변수명,변수명):
    # 함수명

#함수명 짓는 조건은 변수명과 같음
# 변수 : 데이터 담는 그릇 => 명사형
# 함수 : 액션들을 모아 놓은 => 동사형
age =10
def yaDambae():
    print("hi")

# 2) 함수 호출
yaDambae()

def test():
    pass # 들여쓰기 들어가서 자리만 차지하는

def printSum(a,b=99):
    print(a)
    print(b)
    print(a+b)
printSum(10)

def printSum(x):
    print(x)

printSum(100)
printSum(100)



def hi(a=500,b=200):# 파이썬은 파라미터 지정 가능
    print("HI")
hi()

# 일반 언어 메소드 오버로딩: 일부러 함수명을 같게 짓는 기술명
# 파라미터(개수, 자료형) 다르면 같은 함수명 가능

# 파이썬 함수 호출 시 구분 불가
# 파이썬은 오버로딩 불가
# def print(txt,end='\n'):
#     print("hi")

# def printhi(a,b,c):
#     print("hi")
#     print(a+b+c)
# printhi(10,20,30)

# def printhi(a,b,c,d):
#     print("hi")
#     print(a+b+c+d)

# printhi(10,20,30)
# printhi(10,20,30,40)