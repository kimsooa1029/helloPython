import random
count = 1
comp_num = random = random.randint(10, 99)
#print(comp_num)
print("1부터 100사이의 숫자를 맞추시오")
while True :
    user_num = int(input("숫자를 입력하시오"))
    if comp_num == user_num:
        print("정답입니다.축하합니다.")
        break
    elif comp_num > user_num:
         print("숫자가 작습니다. 큰 수를 입력하세요")
    else :
         print("숫자가 큽니다. 작은 수를 입력하세요")
         count  = count +1
         
print(count, "한번에 맞추셨네요")
