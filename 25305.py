n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

print(arr[m-1])