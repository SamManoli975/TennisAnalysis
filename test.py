# a =1
# b = 1
# while a <= 5:
#     b =1
#     while b<=12:
#         print(f"{a} by {b} is {a*b}")
#         b = b+1
#     a = a+1


arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n // 2):

    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

print(arr)


arr = arr[::-1]
print(arr)

# arr.reverse()
# print(arr)
