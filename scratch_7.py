#this is a count down loop starting at 20 to 2 stepping -2
for varl in range (20,0,-2):
        print(varl)
#program will count down
else:
    print("enough with loops")

    cars = ["vw","bmw","ford","mazda","tata"]
    for Mycars in cars:
        if Mycars=="ford":
            continue
        print(Mycars)
        for class2 in "lifechoices":
            print(class2)
    bikes = ["suzuki","kawasik","honda","ducatti","vuka"]
    for Mycars1 in cars:
            for mybikes in bikes:
             print(Mycars1,mybikes)