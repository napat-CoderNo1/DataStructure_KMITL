def sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def combination(arr):
    def combo_recur(arr, n):
        if n == 0:
            return [[]]
        combo = list()
        for i in range(len(arr)):
            strt = arr[i]
            rem = arr[i + 1 :]
            for j in combo_recur(rem, n - 1):
                combo.append(sort([strt] + j))
        return sort(combo)

    res = list()
    for i in range(1, len(arr) + 1):
        res.extend(combo_recur(arr, i))
    return res


inp = input("Enter Input : ").split("/")
tot = int(inp[0])
lst = [int(x) for x in inp[1].split()]
sublst = combination(lst)
res = []
for i in sublst:
    if sum(i) == tot:
        res.append(i)
if res:
    for i in res:
        print(i)
else:
    print("No Subset")