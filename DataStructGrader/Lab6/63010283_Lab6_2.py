def length(txt):
    if txt == "":
        print("")
        return 0
    if txt[1:] != "":
        print(txt[0], end='')
        print("*", end='')
        print(txt[1], end='')
        print("~", end='')
        return 2 + length(txt[2:])
    elif txt[1:] == "" :
        print(txt[0], end='')
        print("*")
        return 1

txt = input("Enter Input : ")
print(length(txt))