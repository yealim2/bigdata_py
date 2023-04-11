##리스트 append, pop, insert, remove##

president = ["이승만","윤보선","박정희","최규하","전두환"]

print(president)

n = len(president)
print(n)

president.append("노태우") #데이터 추가
print(president)

president.append("김영삼")
print(president)

president.pop(0)    #데이터 제거
print(president)

president.pop(2)
print(president)

president.insert(0, "이승만")    #인덱스 데이터 추가
print(president)

president.insert(3,"최규하")
print(president)

president.remove("이승만")     #해당 데이터 삭제
print(president)


a = []

for x in range(10):
    a.append(int(input("값을 입력하세요 : ")))

print (a)

for x in range(10):
    a.pop()
    print(a)














