# 반복
# 횟수 : 푸시업 100개
# 조건 : 푸쉬업 점심먹고 5교시
# 
# python
# 컬랙션 탐색용 : for
# 조건 따져서 반복 : while

# for 변수명 in 컬랙션명:
#     내용
# 
""" a = [1,2,3,4,7,6]
for v in a:
    print(v) """
b=range(1,5)
b=list(b)
for vv in b:
    print(vv)
# =>
for vv in range(1,5):
    print(vv)

n=1
for i in range(1,11):
    n *=i
print(n)

b = [1,231,2,3]
# len(b) =4
for i in range(len(b)):
    print(b[i])

# 값 인덱스
for v in enumerate(b):
    print(v,type(v))

# 딕셔너리 순서개념X =>for문 연관 X
# python은 연관 O
c ={"기온":20,"습도":80,"미세먼지":"심함"}
for k,v in c.items():
    print(k,v)

# value = 5
# if value >= (1 << 3):
#     print("24시간")
#     value -= (1 << 3)

# if value >= (1 << 2):
#     print("흡연실")
#     value -= (1 << 2)

# if value >= (1 << 1):
#     print("#주차장")
#     value -= (1 << 1)

# if value >= (1 << 0):
#     print("와이파이")
#     value -= (1 << 0)


def loc(value):
    for i in range(4):
        if value & (1 << i):
            if i == 0:
                print("와이파이")  
            elif i == 1:
                print("주차장")
            elif i == 2:
                print("흡연실")
            elif i == 3:
                print("24시간")
loc(1)