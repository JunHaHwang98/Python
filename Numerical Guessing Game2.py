num = 76

while True:
    guess = int(input("숫자를 입력하세요: "))
    if guess == num:
        print("정답입니다.")
        break
    else:
        print("틀렸습니다,")
