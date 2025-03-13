# 위 -> 아래, 왼쪽-> 오른쪽 순서
#

#조건,반복,컬랙션,특징 => 웹 데이터 활용

# 조건 따져서 소스 흐름 제어
# 일반언어 : if문 세트, switch세트 
# python : if문 세트

#중간
#기말
#평균
def score(a,b):
    c = a+b
    d = int(c/2)
    return print(d)
score(80,90)

def score1():
    a = int(input("중간"))
    b = int(input("기말"))
    c = (a+b)/2
    if c >80:
        print("잘했다")
    return print(c)
score1()

# P : 프로그래밍 / B*D 분석용 툴
# 인터프리터 : 한줄씩 기계어로 변환
# 컴파일러 : 전체를 기계어 변환 => 나중에 실행
avg = 90
if avg > 80:
    b=10
    print("잘했다")
else:
    print("야")

if avg >= 90:
    print("수")
elif avg >= 80:
    print("우")
else:
    print("HI")

# 게임에서는 모서리에서 두 벽에 닿는 경우가 생겨
# if elif (x) if if ~
""" if 오른쪽 벽에 닿아:
    왼쪽으로
if 바닥에 닿아:
    위로
if 왼쪽에 닿아:
    오른쪽으로
if 위에 닿아:
    아래로 """

# 조건식이 많으면 무조건 elif? NO
# if에 해당하면 아래는 보지 않아  if와 elif 동시에 해당하면?
# 마지막은 무조건 else?


print(b)
# 파이썬은 다른언어가 말하는 scope가 무의미

