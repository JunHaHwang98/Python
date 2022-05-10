num = 76

while True:
    guess = int(input("1부터 100 사이 숫자를 입력하세요: "))
    if guess == num:
        print("정답입니다.")
        break
    elif guess > num:
        print("더 작은 수 입니다.")
    else:
        print("더 큰 수 입니다.")
