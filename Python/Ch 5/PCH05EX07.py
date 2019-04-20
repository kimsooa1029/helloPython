import random
lotto_num =  random.randint(10, 99)
#print(lotto_num)

user_num = int(input("복권번호를 입력하시오(0에서 99사이)"))

if lotto_num == user_num :
    print("상금 100만원")
elif  (lotto_num // 10 == user_num // 10) or (lotto_num % 10 == user_num % 10) :
    print("상금은 50만원입니다.")
else :
    print("상금 0원")
