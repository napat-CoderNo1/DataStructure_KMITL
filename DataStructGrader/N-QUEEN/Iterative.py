#Permutations mapped to the board
'''
Permutations of 8 queens, 1 queen per row. 
Can we do better than the previous? Of course! 
If we only take care of the permutations of the numbers 1 to 8, 
and map the first place to row 1, the second place to row 2, 
and so on, we do not worry anymore about being in the same 
row or being in the same column. The total arrangements in this 
case is 8! = 40,320, 416 times better than the previous!
https://python.plainenglish.io/coding-the-8-queens-problem-in-python-d168f8df844b
'''


from itertools import permutations
import timeit

N = 4

def print_table():
    for row in range(N):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(N):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= (N-1) and x+m <= (N-1):
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= (N-1):
                table[y-m][x+m] = 1
            if y+m <= (N-1) and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False

time_start = timeit.default_timer()

table = [[0]*N for _ in range(N)]   
number = [i for i in range(N)]
perms = permutations(number)


num_comb = 0

for perm in perms:
    for index in range(0, N, 1):
        if put_queen(perm[index], index) == True:
            if index == N-1:
                # print_table()
                num_comb += 1
                print(f"solution{num_comb}")
                print(" ")
        else:
            break
    
    table = [[0] * N for _ in range(N)]

time_stop = timeit.default_timer()
print("Input : ", N)
print('number of solutions = ', num_comb)
print("Start time : ",time_start,"Stop time : ", time_stop)
print("Elapsed time during the whole program in seconds:", time_stop-time_start)

'''
if put_queen(perm[0], 0) == True:
        if put_queen(perm[1], 1) == True:
            if put_queen(perm[2], 2) == True:
                if put_queen(perm[3], 3) == True:
                    if put_queen(perm[4], 4) == True:
                        if put_queen(perm[5], 5) == True:
                            if put_queen(perm[6], 6) == True:
                                if put_queen(perm[7], 7) == True:
                                    print_table()
                                    num_comb += 1
                                    print(f"solution{num_comb}")
                                    print(" ")
'''