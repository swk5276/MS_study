value = 1
# 1이면 와이파이
# 2면 주차장
# 4면 흡연실
# 8이면 24시간

# 3이면 와이파이 주차장
# 12이면 흡연실 24시간
# 13 흡연실 24시 와이파이
# 7 흡연실 주차장 와이파이
def location():
    n = int(input())
    a1= "와이파이"
    a2= "주차장"
    a3= "흡연실"
    a4= "24시간"
    if n==1:
        result =a1
    elif n==2:
        result =a2
    elif n==4:
        result =a3
    elif n==3:
        result =a1+a2
    elif n==8:
        result =a3+a4
    return result
print(location())

def check_condition(n):
    # 각 숫자에 해당하는 옵션을 미리 딕셔너리로 정의
    options = {1: "와이파이", 2: "주차장", 4: "흡연실", 8: "24시간"}
    
    # 선택된 옵션을 저장할 리스트
    result = [name for value, name in options.items() if n & value]

    return " + ".join(result) if result else "선택된 옵션 없음"

def location():
    n = int(input())
    
    result = ""
    
    if n & 1: result += "와이파이 + "
    if n & 2: result += "주차장 + "
    if n & 4: result += "흡연실 + "
    if n & 8: result += "24시간 + "
    
    return result[:-3] if result else "선택된 옵션 없음"

print(location())


def location():
    n = int(input())

    a1 = "와이파이"
    a2 = "주차장"
    a3 = "흡연실"
    a4 = "24시간"

    result = ""

    if n >= 8:
        result += a4
        n -= 8
        if n > 0:
            result += " + "
    
    if n >= 4:
        result += a3
        n -= 4
        if n > 0:
            result += " + "
    
    if n >= 2:
        result += a2
        n -= 2
        if n > 0:
            result += " + "
    
    if n >= 1:
        result += a1

    return result if result else "선택된 옵션 없음"

print(location())

