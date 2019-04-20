count = 1
sumAll = 0

while True :
    num = int(input("숫자를 입력하세요"))
    sumAll = sumAll + num
    yesno = input("계속 가로 열고 (yes/no)")
    if yesno == "no":
               break
    count = count + 1
agv = sumAll / count

print("합계 :" , sumAll)
print("평균 :", agv )
