import random

position = ["가운데", "오른쪽", "왼쪽"]


com_pos = random.choice(position)
#print(com_pos)
user_pos= input("위치를 선택하세요(가운데, 오른쪽, 왼쪽)")

if com_pos == user_pos:
    print("노골입니다.")
else :
    print("골입니다.")
