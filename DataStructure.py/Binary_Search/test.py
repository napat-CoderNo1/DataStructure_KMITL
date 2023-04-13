def binarySearch(arr, x, low, high):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        elif arr[mid] == x:
            return mid
    return -1

x = 2
#      0 1 2 3 4
arr = [1,2,3,4,5]
low = 0
high = len(arr)-1

print(binarySearch(arr, x, low, high))