# 이름 :
# 키 :
# 몸무게 :
# BMI :
# ~씨는 비만

def BMI():
    name = input("이름:")
    height = int(input("키"))
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

#소스가 김
# if bmi > 20:
#   print("고도비만")
#변수 사용 => 소스가 짧음 => 램을 많이 먹음
# if bmi > 20:
#   result = "고도비반"
#