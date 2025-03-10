# type casting [형 변환]
# 메뉴 
# 가격
# 파이썬은 str로 받아야 글자든 숫자든 다 소화
# 어디서 데이터 받아오면 다 str

menu = input("메뉴명\t")
# price = input("가격\t")
price = int(input("가격\t")) 
# 형 변환하면 다른 번지에 int 생성
# 가비지 컬렉터로 str 메모리 해제
# int , float, str, list
# np.array, torch.
print(menu,type(menu))
print(price,type(price),id(price))
print("%d짜리 %s먹자"% (price,menu))
#print(price+"짜리"+menu+"먹자")