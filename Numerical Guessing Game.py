num = 76
print("숫자게임에 오신 것을 환영합니다.")
guess = int(input("1부터 100 사이의 숫자를 추측해보세요: "))

if guess == num:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
