#Function3.py
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(6,6))

#키워드, 인자
def userURL(server,port):
    strURL="http://"+server+":"+port
    return strURL

#호출
print(userURL("credu.com","80"))
print(userURL(port="8080",server="credu.com"))

#가변인자는 입력되는 인자의 개수가 가변적인 경우
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM","ZZAMPPONG"))

#정의되지 않은 인자 처리
def userURLBuilder(server, port, **user):
    strURL = "http://"+server+":"+port+"/?"
    for key in user.keys():
        strURL+=key+"="+user[key]+"&"
    return strURL

#호출
print(userURLBuilder("naver.com","80",id="KIM",password="1111"))
print(userURLBuilder("naver.com","80",id="KIM",password="1111",name="homer",age="40"))

#람다 함수 (간단하게 함수를 정의, 익명함수)
g=lambda x,y:x*y

print(g(3,4))
print(g(5,6))
#메모리에 있는 변수, 함수를 딕셔너리
print(globals())