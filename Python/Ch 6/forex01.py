breads = ["호밀빵", "위드", "화이트"]
meats = ["미트볼", "소시지", "닭가슴살"]
vegies = ["양상추", "토마토", "오이"]
sauces = ["마요네즈", "허니 머스타드", "칠리"]
count = 1

for b in breads:
    for m  in meats:
        for v in vegies:
            for s in sauces:
                print (count , ":", b, "+", m, "+", v, "+", s)
                count += 1
