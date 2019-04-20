#add (a, b)
#sub(a, b
#mult(a, b)
#div(a,b)


    
def add (a, b):
    print ("(",a, "+",b, ") =" ,a+b)
def sub (a, b):
    print ("(",a, "-",b, ")=" ,a+b)
def mult (a, b):
    print ("(",a, "*",b ,")=" ,a+b)
def div (a, b):
    print ("(",a, "/",b, ")=" ,a+b)

first = int(input("첫번쨰 수를 입력하세요"))
second = int(input("두번쨰 수를 입력하세요"))
sym = input("사칙연산중 하나를 입력하세요")

if sym == "+":
    result = add (first, second)
elif sym == "-":
    result = sub (first, second)
elif sym == "*":
    result = mult (first, second)
elif sym == "/":
    result = div (first, second)
