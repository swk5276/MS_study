# 함수 사용이유 : 소스 정리 차원 => 사람 관점에서 가독성 위하여
# 컴퓨터 관점에서는 느려짐
# 메모리 관리 관점 => 유지 보수 관점

# 함수 정의
# ~하고
# 함수 호출 [jump연산 => 물리적으로 이동 => 시간이 걸림]
# 재귀함수 사용 시 함수 사용 증가 => 계산용 X => 반복문 사용 O
# 

# 개발자 목표 : A프로젝트 => 해결 가능한 제일 간단한
# 재귀 사용 : 사용자로부터 원하는 입력 받을 때까지 반복
import re

def HI():
    print("HI")
HI()
def getHeight():
    h = input("키 : ")
    h = float(h)
    if h > 200:
        print("다시 입력!")
        return getHeight()
    return h

def BMI():
    name = input("이름:")
    height = getHeight()
    weight = int(input("몸무게"))
    BMI = weight/(height/100)**2
    if BMI >= 39:
        return print(name,"고도 비만",BMI)
    elif BMI >= 32:
        return print(name,"중도비만",BMI)
    elif BMI >= 30:
        return print(name,"경도비만",BMI)
    elif BMI >= 24:
        return print(name,"과체중",BMI)
    elif BMI >= 10:
        return print(name,"정상",BMI)
    else:
        return print(name,"저체중",BMI)
BMI()

