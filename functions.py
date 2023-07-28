x = 1


def myfunction():
    #global x
    x = 2
    print("in myfunction before if, x ist ",x)
    if x == 2:
        x = 3
        print("in if von myfunction(), x ist ", x)
    print("in myfunction nach if, x ist ", x)


myfunction()

print("ausserhalb von myfunction(), x ist ",x)

try:
    x = 3/0
except ZeroDivisionError as ex:
    print("Zerodivisionerror ",ex)
except Exception as ex:
    print("Exception is ", ex)
else:
    print("In else ")
finally:
    print("finally always printed")


