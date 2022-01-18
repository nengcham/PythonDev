# 3개의 숫자를 입력받아 세 숫자의 합, 세 숫자의 곱, 세 숫자 정렬출력
# 단, 세개의 숫자가 겹치면 안되고 겹치면 다시받아야됨
# 1. 숫자가 겹치지 않게하기
# 2. 합, 곱, 정렬

num1 = input("첫 번째 숫자를 입력해주세요: ")
num2 = input("두 번째 숫자를 입력해주세요: ")

while num1 == num2:
    print("숫자가 중복됩니다. 다시 입력해주세요.")
    num2 = input("두 번째 숫자를 입력해주세요: ")

num3 = input("세 번째 숫자를 입력해주세요: ")

while num2 == num3 or num3 == num1:
    print("숫자가 중복됩니다. 다시 입력해주세요.")
    num3 = input("세 번째 숫자를 입력해주세요: ")

sum = int(num1) + int(num2) + int(num3)
mul = int(num1) * int(num2) * int(num3)
li = [int(num1), int(num2), int(num3)]
print(f"입력한 숫자는 {li}입니다.")
print(f"입력한 숫자의 합은 {sum}입니다.")
print(f"입력한 숫자의 곱은 {mul}입니다.")
li.sort()
print(f"입력한 숫자정렬: {li}.")

