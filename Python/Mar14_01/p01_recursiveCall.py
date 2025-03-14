def Sum(N):
    sum=0
    for i in range(N+1):
        sum+=i
    return print(sum)
Sum(4)

def Sum2(N):
    if N > 0:
        N += Sum2(N - 1)
        # N -= 1
    return N

print(Sum2(5))

# 함수를 재귀적으로 호출 : 기술명
#   함수 내부에서 자기 자신 호출해서 반복
#   언제 사용? : 규칙적인 숫자 계산 시 사용 X => 속도 느림
#   => 

# 팩토리얼

def Fac1(N):
    if N != 1:
        N*= Sum2(N - 1)
        return N
    return 1
print(Fac1(5))

def Fac(x):
    if x != 1:
        return Fac(x-1)*x
    return 1
print(Fac(5))

# 피보나치 수열
# 1 => 1 => 2 => 3 => 5 => 8 => 13
# fibo(1)=1 fibo(2)=1 fibo(3)= 2
# fibo(3) = fibo(1)+fibo(2)
# fibo(4) = fibo(2)+fibo(3)

# 재귀 제한횟수 설정
import sys
sys.setrecursionlimit(100000)
def Fibo(N):
    if N <3:
        return 1
    return Fibo(N-2)+Fibo(N-1)
print(Fibo(6))

