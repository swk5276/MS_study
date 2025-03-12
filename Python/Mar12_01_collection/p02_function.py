
# def test(a, b):
#     print("green",a,b[0])
    
#     a=100 #지역 변수
#     b[0]=100
#     print("green",a,b[0])

### 전역 변수 선언 ###
# a = 10 # 스택 : int, 값 자체 저장
# b = [10,20]  # 스택: 리스트 힙 메모리를 가리킴 # 힙: 리스트 객체

# print("red",a,b[0]) # 전역 변수 값 출력

# test(a,b) 
# a = 10 [call by value]
# b = [10,20] [call by reference]

#test(a,b) 종료 : a는 제거, b는 유지

# print("red",a,b[0])

# call by value , call by reference
# 값을 넣어 호출이냐?, 주소값을 넣어 호출이냐
# 파이썬은 call by reference 만 존재

##########################
def test(a, b, c):
    global e # 이 공간은 외부의 e
    print("함수", a, b[0], c[0])  
    a = 100 # 지역 변수 a 새롭게 생성
    b[0] = 100 # 리스트 b의 첫번째 원소 변경 [원본 변경]
    c = [100, 200] # 새로운 리스트를 만들어 지역 변수 C가 참조[전역 c와 무관]
    d = 100
    e = 100
    print("함수", a, b[0], c[0], d, e)
##########################
a = 10
b = [10, 20]
c = [10, 20]
d=10
e=10
print("외부", a, b[0], c[0],d,e)
test(a, b, c)
print("외부", a, b[0], c[0], d, e)  # 여기서 d, e는 test() 내부 변수이므로 오류 발생 가능
