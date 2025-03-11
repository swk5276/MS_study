# 연산자
# = : 대입 연산자
# 우항에 있는 거 좌항에 넣어라
# 우선순위 마지막
# x = int(input("x:"))
# y = int(input("y:"))
# print("x는 %d, y는 %d"%(x,y))

# 산술 연산
# /은 실수 나누기 , //가 정수 나누기
x=3
y=2
a = x+y
b = x-y
c = x*y
d = x/y
e = x//y
print(a,b,c,d,e)

z = "ㅋ"
zz = "ㅋㅋ"
# g = x+z
h = z+zz
# print(g)
print(h)

i = x*z
print(i)

j = x**y
print(j)

x +=3
y = y*2
#y *=2
print(x,y)

# 다른언어 ++,--
# 파이썬에는 없음
# python : 인간 친화적 => 공부할 거리 줄이기
# x = x+1

#shift 연산자
x = 4
y = 3
z = x << y
print(z)

# 글 정렬
# left = 1
# right = 3
# center = 2

# 글 속성
#   이탤릭 = 1 << 0 = 1
#   굵게 = 1 << 1 = 2
#   밑줄 = 1 << 2 = 4

#####################################
조건 = 5  # 와이파이(1) + 주차장(4)

와이파이 = 1 << 0  # 1
흡연실 = 1 << 1  # 2
주차장 = 1 << 2  # 4

# 특정 조건 포함 여부 확인
if 조건 & 와이파이:
    print("와이파이 있음")
if 조건 & 흡연실:
    print("흡연실 있음")
if 조건 & 주차장:
    print("주차장 있음")

#########
# 구매 물건가: 47850
# 낸 돈 : 50000
# 거스름돈 : 2150
# 5만원 : 0 / 1만원 : 0 / 5천원 : 0 / 천원 : 2개
# 
# a = int(input("구매물건가:"))
# b = int(input("낸 돈 : "))
# c = b-a
# print("거스름돈:%d"%(c))
# print("5만원",c//50000,"만원", c//10000,"5천원",c//5000,"천원", c//1000)

# 단위 = 1000
# 개수 = 거스름//단위
# print
# 거스름 %= 단위

#########
# 바퀴 둘레:
# 앞 기어 톱니수:
# 뒤 기어 톱니수:
# 발 구른 횟수:
# 이동 거리:

# meter = int(input("둘레"))
# front = int(input("앞 기어"))
# back = int(input("뒤 기어"))
# foot = int(input("구른 횟수"))
# print("이동거리는 %d"%(front/back*meter*foot))

# 키, 나이
height = 160.2
age = 5
print("키는 %.1f 나이는 %d"% (height,age))

b = age < 10
# b = 10 > age
print(b)

c = age==5
print(c)

a =10
b =a+5
# 10은 Heap 영역에 객체로 저장되고, a는 Stack에 저장된 변수(참조)로 10을 가리킴.
# a + 5를 수행하면 15라는 새로운 정수 객체가 Heap에 생성되고, b가 이를 참조.
age == 5

# 일반언어 : &&[앞에확인 후 뒤 판단] , &[무식하게 앞 뒤 둘다 확인], ||
# 파이썬 : and, or, &, |
# xor : ^
# 실행 속도 차이 :
# and : 확률 낮은 것을 앞으로
# or : 확률 높은 것을 앞으로

d = (height>=130) and (age>=5)
print(d)

# e는 나이가 50살이거나, 키가 140이상이면
e = (age >=5) or (height>=140)
print(e)

# f는 나이가 10살이상,20살이상
f = (age>=20)
print(f)


# g는 100 <= 키 <= 130만 탈수있는
# c언어

# 파이썬
g = (100 <=height<=130)
print(g)

# h는 나이가 5살 이상
# 키가 130cm 이하든지
# 둘중에 하나만
h = (age>=5)^(height<=130)
print(h)
# i는 h탈 수 있는 사람 못 타
# i는 h의 반대

# not
# 일반 언어: !
# 파이썬 : not 값
# i는 h탈 수 있는 사람 못 타, h 못타는 사람 타
# i는 h의 반대
# i는 h의 반대
i = not h # 1항 연산자
print(i)

# C
# java
# 3항연산 : ?
# 파이썬 3항 연산 없음
# say = (age >= 10 )? "타세요":"나가요"

if age >= 10:
    say= "타세요"
else:
    say = "나가"
print(say)

#
