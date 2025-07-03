num = 0 
while True:
    while True:
        try:
            play = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): '))
            if play > 3 or play < 1:
                print("1, 2, 3중 하나를 입력하세요")
                continue
            break
        except ValueError:
            print("정수를 입력하세요")
    for i in range(play):
        num += 1
        if num > 31:
            print("playerB win!")
            break
        print(f"playerA:{num}")
    if num > 31:
            break
    while True:
        try:
            play = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): '))
            if play > 3 or play < 1:
                print("1, 2, 3중 하나를 입력하세요")
                continue
            break
        except ValueError:
            print("정수를 입력하세요")
    for i in range(play):
        num += 1
        if num > 31:
            print("playerA win!")
            break
        print(f"playerB:{num}")
    if num > 31:
            break