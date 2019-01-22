def spam():
    yield"first"
    yield"second"
    yield"third"



for x in spam():
    print (x)