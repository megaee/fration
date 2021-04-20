a={'c':3,'t':5}
##b={'c':3,'t':5}
b=None
try:
    for k in a:
        print(k)
        if k in b:
            print("@@@@@")
except TypeError:
    pass
