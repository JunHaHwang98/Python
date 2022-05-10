import random
num = random.randint(1, 999)

print(num)

while True:
    try:
        guess = int(input("1부터 999 까지의 숫자를 입력하세요: "))
        if guess == num:
            print("정답입니다.")
            break
        elif guess > num:
            print("더 작은 수 입니다.")
        else:
            print("더 큰 수 입니다.")

    except:
        print("1-999중의 숫자를 입력하세요: ")
