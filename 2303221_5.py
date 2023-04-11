# 반환형 함수
# 파이썬 타입 선언 필요 x
# 파이썬 무한 정수 취급, 그래서 느리다

# C언어의 경우
"""
#include <stdio.h>

float func(float n, float m)
{
    return x / y;
}


int main()
{
    float q = func(10.22, 20.555);
    return 0;
}
반환값이 정수면 int func()
인수가 있으면 int func(int x, int y)
"""


def f(x,y):
    return x * y

z = f(3.56, 7.11)
print(z)

z = f(65.43, 88.90)
print(z)



# 매개변수 x, 반환값 x

def myprinting():
    print("두개의 정수를 입력하세요")
    print("덧셈결과가 출력됩니다")

# 매개변수 x, 반환값 o

def inputnumber():
    num = int(input("정수를 입력하세요 : "))
    return num

# 매개변수 o, 반환값 o

def addnum(x,y):
    return x+y

# 매개변수 o, 반환값 x
def result (z):
    print("두 정수의 합은 %d입니다." %z)

# main 함수

myprinting()
a = inputnumber()
b = inputnumber()
print(a,b)
c= addnum(a,b)
print(c)
result (c)
    















