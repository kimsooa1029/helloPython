username = "dream"
password = "1234"
while True :
    name = input ("id를 입력하세요")
    psd = input ("암호를 입력하세요")
    if username ==name and password ==psd:
        print("로그인 성공")
        break
    else:
        print("id 또는 암호가 틀렸습니다.")
