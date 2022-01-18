# 국어, 영어, 수학 점수를 입력받아 
# 평균점수 60이상, 과목당 40점 이상일때 합격 아니면 불합격

num1 = input("국어: ")
num2 = input("영어: ")
num3 = input("수학: ")

kor = int(num1)
eng = int(num2)
math = int(num3)

sum = kor + eng + math
avg = (kor + eng + math) / 3

if kor > 40 and eng > 40 and math > 40 and avg > 60 :
    print("합격입니다.")
else :
    print("불합격입니다.")



