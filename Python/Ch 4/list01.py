a_list = [34, 25.6, "김수아"]

print(a_list)
print(a_list[0])
print(a_list[1])
print(a_list[2])

a_list.append ("이순신")
print(a_list[3])
print(a_list[:-1])
#-는 뒤부터, +는 앞부터 실행시키는 모드다.
#append 뒤에 붙이다. -> 리스트 뒤에 추가하기

print(a_list[1:3])
print(a_list[:2])
print(a_list[:])
#처음부터 실행시키고 싶으면 0을 굳이 안써도 된다.
