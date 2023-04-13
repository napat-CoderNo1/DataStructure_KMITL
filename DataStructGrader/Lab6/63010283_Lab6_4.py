def pantip(k, n, arr, path):
    count = 0
    if n == len(arr):
        if k == sum(path):
            print(*path, sep=' ')
            return 1
        return 0
    count = count + pantip(k,n+1,arr,path+[arr[n]]) 
    count = count + pantip(k,n+1,arr,path) 
    return count

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))