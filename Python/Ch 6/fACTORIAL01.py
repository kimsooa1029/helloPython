fact = int(input("원하는 Factorial 값을 입력하세요"))
result = 1
for i in range (1, fact+1):
    result = result * i
print ("결과 : ", result )
