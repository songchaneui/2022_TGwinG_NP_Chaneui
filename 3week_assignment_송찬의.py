# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
from time import time


def question1():
    answer = "next"
    return answer

# 문제 2번
def leapYear(year):
    if (year % 4)==0:
        if(year%100)==0:
            if(year%400)==0:
                return "윤년입니다."
            else:
                "윤년이 아닙니다."
        else:
            return  "윤년입니다."
    else:
        return "윤년이 아닙니다."

# 문제 3번
def alram(time):
    time = int(time)
    if (time % 100) >= 45:
        altime = time - 45 
    else:
        altime = time -85
    if (altime >= 1200):
        altime = str(altime)
        x = "오후"
        y = altime[0:2]+"시"
        z = altime[2:]+"분"
        return x + y + z
    else:
        x = "오전"
        if (altime >= 1000):
            altime = str(altime)
            y = altime[0:2]+"시"
            z = altime[2:4]+"분"
        else:
            altime = str(altime)
            y = altime[0:1]+"시"
            z = altime[1:3]+"분"
        return x + y + z
print(alram(input("시간을 입력하세요: ")))

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    if x1 = x2 and y1 = y2:
            if r1 = r2:
                return "어딘지 모르겠다 오바"
            else:
                return "0"
    elif x1 + x2 = 0 or y1 + y2 = 0:
        return "1"
    else:
        return "2"
