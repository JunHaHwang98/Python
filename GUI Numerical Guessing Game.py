import random
import tkinter

number = random.randint(1, 100)

print(number)

print("숫자 게임에 오신 것을 환영합니다!")

while True:
    guess = int(input("1부터 100사이의 숫자를 입력하시오: "))
    if guess == number:
        print("정답입니다.")
        break
    elif guess > number:
        print("더 작은 수 입니다.")
    else:
        print("더 큰 수 입니다.")
