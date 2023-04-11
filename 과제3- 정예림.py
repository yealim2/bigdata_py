# 4가지 형태 함수 프로그램

# 함수의 4가지 조건
# 매개변수 없음,  반환값 없음
# 매개변수 있음, 반환값 없음
# 매개변수 없음 , 반환값 있음
# 매개변수 있음, 반환값 있음

# 일반적인 함수
def add(a,b):
    return a+b

a= add(3,4)
print(a)

# 입력값이 없는 함수
def cat():
    return "Meow"

a=cat()
print(a) 

# 결과값이 없는 함수
def add(a,b):
    print("%d와 %d의 합은 %d 입니다."%(a,b,a+b))

add(3,4)


#입력값과 결과값이 둘다 없는 함수
def cat():
    print("Meow")

cat()
