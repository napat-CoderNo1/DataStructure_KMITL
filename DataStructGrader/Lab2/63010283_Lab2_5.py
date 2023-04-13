import string

def bon(w):
    for i in range(len(w)):
        if w[i] == w[i+1]:
            for j in range(len(string.ascii_lowercase)):
                if w[i] == string.ascii_lowercase[j-1]:
                    return j*4
                    

secretCode = input("Enter secret code : ")
print(bon(secretCode))