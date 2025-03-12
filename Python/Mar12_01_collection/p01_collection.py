# list : 주력으로 사용
from sys import stdout


a = [1,1,1,1,2,3,4,6]
# set : 중복 x, 순서 때문에 잘 안쓰임
a = set(a) # list => set
print(a)
a = list(a)
print(a)

# 학생 조회 시
# 번호 : 3 => list 사용
# 이름 : 철수 => dict 사용[순서 X]

# Json과 형태 유사
student = {"홍길동":[100,90,80],
           "김길동":[50,30,10],
           "이길동":[30,10,0]}
print(student["김길동"])
# 홍길동 국어 점수
print(student["홍길동"][0])
# 유지보수
# 2차원 넘기지 않도록
print(list(student.keys()))

print("최길동" in student)

#list,set,dict
#range : 범위
a = range(5)
a = range(1,15)
a = range(1,15,2)
print(a,type(a))

# list 1~20
b = range(1,20)
b = list(b)
print(b)

# tuple : 중복x
# 데이터 여러개 저장용 X
# 변수 여러개 한꺼번에 값 넣을때
c = (10,10,20,30,40)
print(c[2])

### 자리 바꾸기
##c언어에서는
q =100
w =200
# e=q
# q=w
# w=e
# print(q,w)
##python에서는
(q,w) = (w,q) #가로는 생략 가능
print(q,w)

t,y,u = 120,123,150
print(t,y)







