import random
first_num = random.randint(2, 10)
second_num = random.randint(2, 10)
quest = str(first_num) + "*" + str(second_num) +"는"

while True:    
    answer = int(input(quest))
    if(answer == first_num * second_num):
        print ("맞았습니다.")
        break
    else :
        print ("틀렸습니다.")
        answer = int(input(quest))
