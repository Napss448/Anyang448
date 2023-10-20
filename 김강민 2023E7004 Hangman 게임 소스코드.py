from random import choice

# 단어 목록
words = ["apple", "banana", "orange", "cherry", "melon", "peach"]

# 무작위로 단어 선택
word = choice(words)

letters = set()  # 플레이어가 입력한 알파벳 저장 (set을 사용하여 중복 입력 방지)
attempts = 6  # 최대 시도 횟수

print("Hangman 게임을 시작합니다!")

# 정답을 맞힐 때까지 무한 반복
while True:
    succeed = True  # 성공 여부 확인 변수
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False

    print()

    if succeed:
        print("승리! 정답은", word, "입니다.")
        break

    letter = input("한 글자를 추측하세요: ").lower()  # 플레이어로부터 한 글자씩 입력
    if len(letter) != 1 or not letter.isalpha():
        print("올바른 글자를 입력하세요.")
        continue

    if letter not in letters:
        letters.add(letter)

    if letter in word:
        print("정답입니다!")
    else:
        attempts -= 1
        print("틀렸습니다!")
        print("남은 목숨:", attempts)
        if attempts == 0:
            print("목숨을 모두 잃었습니다. 정답은", word, "입니다.")
            break