try:
    try:
        print("start code")
        #print(asff)
        print("No errors")
    except SyntaxError:
        print("We have an error Syntax")
except NameError as error:
    print(error)
else:
    print("No problem")
print("code after capsule")