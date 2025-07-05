import random
num = 0 

def brGame():
    global num
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
        print(f"player:{num}")
        if num >= 31:
            print(f"computer win!")
            return True 
    return False

def computer():
    global num
    ans = random.randint(1, 3)
    for i in range(ans):
        num += 1
        print(f"computer:{num}")
        if num >= 31:
            print(f"player win!")
            return True 
    return False

cnt = 0
while True:
    if cnt % 2 == 0:
        if brGame():
            break
    else:
        if computer():
            break
    cnt += 1
