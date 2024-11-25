def person(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)

person('Navin', age=28, city='Moscow', mob=3055494152)