n = 1234
sum = 0
while n > 0 :
    dight = n % 10
    sum = sum + dight
    n = n // 10
print(sum)
