import random
first = random.randint(1, 100)
second = random.randint(1, 100)
quest = str(first) +"-" + str(second) +"="
user_input = int(input(quest))
answer = first - second

if user_input == answer :
    print("정답")
else :
    print("오답")
