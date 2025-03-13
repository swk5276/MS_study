# String name = "홍길동";
# System.out.println(name == "홍길동");

# name = input("name:")
# print(name == "홍길동")
# print(name is "홍길동")


# # 스택 : 지역변수 , 함수 호출 시 정보
# # 힙 : 객체(문자열,리스트,딕셔너리)

# # 홀수 판별 함수
# def odd(n):
#     return print(n%2==1)
# odd(3)

# def odd1(n):
#     isOdd = (n%2==1)
#     return isOdd
# odd1(3)

# # 홀수 판별
# def odd2(n):
#     n = int(input("입력:"))
#     if n%2 !=0:
#         return print("홀수")
#     else:
#         return print("짝수")
# odd2(3)

from time import sleep


# def multi(n):
#     return n*2
# b = multi(2)
# sleep(b)

# 어떤 함수의 결과(return)가 여러개 불가
# => collection 하나로 가능
def plus(x,y):
    a= x+y
    b= x*y
    c= x-y
    d= x/y
    e=(a,b,c,d)
    # return e
    # 튜플 형태여서 리턴 여러개 가능
    return a,b,c,d
aa,bb,_,dd= plus(20,30)
print(aa,bb,_,dd)

# => tuple을 사용한 이유는?
(aa,bb,cc,dd)= plus(20,30)
print(aa,bb,cc,dd)

# 튜플은 소괄호 생략 가능
aa,bb,cc,dd = plus(20,40)
print(aa,bb,cc,dd)

# 튜플의 요소를 변수에 할당 (일부 값 무시)


data = (1, 2, 3, 4, 5)
a, b, _, d, e = data  # 3을 무시 (_ 사용)
print(a, b, d, e)  # 출력: 1 2 4 5


# 변수
# 데이터 임시 저장
# 언제 사용?=> 계산기 쓰다 10 누른거 저장할 떄

# return
# 함수 결과 되돌려
# => 웹 게시판을 함수써서 뭔가를 만들면



