# 국어점수 80점
kor = 80
print(type(kor))
# 변수1 = 데이터1
# collection : 변수 하나에 데이터 N개

# C,java 배열 : 수정 불가


s = "안녕하세요 하이"
print(s[2])
print(len(s))
print(s[::-1])

# 일반 언어 :
# list 
# set
# map

eng = [80,30,54,12,10,11,12,14,15]
print(eng)
print(type(eng))
print(len(eng)) #내용물 개수
print(eng[1])
print(eng.index(30))
print(eng[2:5])
print(eng[3:6:2])
print(eng[:6:2])
print(eng[::2])

print(eng)
eng.append(99) # 뒤에 추가
eng.insert(2,88) # 2번자리 88추가
eng[1] =0
del eng[0]
print(eng)

# 수학점수들
# set : 순서 때문에 사용 애매?
# 중복 X가 뭔가 있는
mat ={100,80,50,80,70,100,50,90}
print(mat)
print(type(mat))
print(set(mat))

# dict: 순서개념X, [키-값] 쌍으로 이루어짐
student ={"반장":"홍길동","부반장":"김길동"}
print(student)
print(type(student))
print(student["반장"])
# list: 1->30
# set : 1->?




