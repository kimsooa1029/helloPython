#parameter ; (인수 x)
# 밑에 값이 위로 올라가서 다시 내려오고 2번째 밑의 값이 다시 위로 올라기 내려오는 것

#함수
#parameter 0 return 0
#parameter 0 return x
#parameter x return 0
#parameter x return x

def print_name(name):
    print(name + "님 반갑습니다.")
    print("앞으로 친하게 지내요")

def sum_all(first, second) :
    result = first + second
    return result

print_name ("김수아")
print()
print_name ("김철환")

print()
print()
sum_result1 = sum_all (5, 67)
sum_result2 = sum_all (75, 57)
print(sum_result1)
print(sum_result2)
