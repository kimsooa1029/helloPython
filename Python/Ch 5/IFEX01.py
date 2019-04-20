num = int(input("점수를 입력하세요"))
          
if num > 100 or num <0 :
    print("성적을 잘못 입력하였습니다.")
elif num >= 90:
    print("A 학점입니다.")
    print("축하합니다.")
elif num >= 80:
    print("B 학점입니다.")
    print("축하합니다.")
elif num >= 70:
    print("C 학점입니다.")
elif num >= 60:
    print("D 학점입니다.")
elif num >= 50:
    print("F 학점입니다.")
    print("꿈의학교")



#어떠한 상황에서든지 꿈의학교를 표현하고 싶다면 빽스페이스 누르기

if num > 100 or num <0 :
    print("성적을 잘못 입력하였습니다.")
elif num >= 90 and num <= 100: 
    print("합격입니다.")
    print("축하합니다.")
else :
    print("불합격입니다.")
print("꿈의학교")
