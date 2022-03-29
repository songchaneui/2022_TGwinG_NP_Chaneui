# 문제 1번
def sum(a,b):
    p = a+b
    return p

# 문제 2번
def sub(a,b):
    m = a-b
    return m

# 문제 3번
def mul(a,b):
    c = a*b
    return c

# 문제 4번
def div(a,b):
    d = a/b
    return d

# 문제 5번
def distance(x1,y1,x2,y2):
    dis = {(x1-x2)**2+(y1-y2)**2}**1/2
    return dis

# 문제 6번
def short():
    lylic = "life is short art is long"
    cut = string[8:13]
    return cut

# 문제 7번
def myReverse(string):
   rev = string[::-1]
   return rev
string = input("단어를 입력해주세요:")
print(myReverse(string))
    

# 문제 8번
def letMeIntroduceMyself():
    name=input("이름을 입력하시오:")
    hobby=input("취미를 입력하시오:")
    univ=input("재학 중인 대학을 입력하시오:")
    birth=input("생일을 입력하시오(예시:981128):")
    intro = "제 이름은 {0}입니다. 제 취미는 {1}이구요. 저는 {2}를 다니고 있습니다. 제 생일은 {3}월 {4}일 입니다.".format(name, hobby, univ, birth[2:4],birth[4:6])
    return intro
print(letMeIntroduceMyself())

# 문제 9번
def calcAI():
    first = int(input("첫 번째 숫자를 입력하시오:"))
    second = int(input("두 번째 숫자를 입력하시오:"))
    sum = first + second
    last = "두 수의 합은 {}입니다.".format(sum)
    return last
print(calcAI())
