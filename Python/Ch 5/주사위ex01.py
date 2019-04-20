import random

comp_num = random.randint(1,6)
user_num = int(input("주사위의 숫자를 입력하세요(1-6)"))
if comp_num == user_num:
    print("맞았습니다.")
else:
    print("숫자가 틀렸습니다.")
    user_num = int(input("주사위의 숫자를 입력하세요(1-6)"))
    if comp_num == user_num:
        print("맞았습니다.")
    else:
        print("숫자가 틀렸습니다.")
        user_num = int(input("주사위의 숫자를 입력하세요(1-6)"))
        if comp_num == user_num:
            print("맞았습니다.")
        else:
            print("숫자가 틀렸습니다.")


