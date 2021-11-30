#Function2.py
#함수를 정의 (원본번경)
# def change(x):
#     x[0]="H"

#함수를 정의 (원본미변경)
def change(x):
    x1=x[:]
    x1[0]="H"
    print("함수 내부:",x1)

#함수를 호출
wordlist=["J","A","M"]
change(wordlist)
print("함수 호출 후:",wordlist)

#지역변수와 전역변수(이름충돌)
x=1
def func(a):
    return x+a

#호출
print(func(1))

def func2(a):
    x=2
    return x+a

#호출
print(func2(1))

#글로벌변수 변경
g=1
def testScope(a):
    global g
    g=2
    return g+a

#호출
print(testScope(1))
