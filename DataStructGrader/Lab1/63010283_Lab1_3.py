print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
numbers = []
count = []
check = False

x = input().split()
for i in x:
    x = int(i)
    numbers.append(x)

for i in range(0, len(numbers), 1):
    if numbers[i] > 0:
        check = True

if check == False:
    print("*** No Candidate Wins ***")
    

if check == True:
    for i in range(1,21,1):
        x = numbers.count(i)
        count.append(x)

    for i in range(0, len(count), 1):
        if count[i] == max(count):
            print(i+1)
            break