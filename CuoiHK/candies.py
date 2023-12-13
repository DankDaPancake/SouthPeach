import bisect

fi = open('candies.inp','r')
fo = open('candies.out','w')

n = int(fi.readline())
a = []
layer, sum, i = 0, 0, 1

for i in range(1, 510005):
    layer += i
    sum += layer
    a.append(sum)


def isPossible(arr, k):
    n = len(arr)
    for i in range(n):
        j = bisect.bisect_left(arr, arr[i] + k, i + 1, n)

        if j < n and arr[j] - arr[i] == k:
            return True
    return False

if n == 0:
    fo.write('YES')
    exit()
if n > 10000000000000000:
    fo.write('YES')
    exit()
if isPossible(a, n):
    fo.write('YES')
else:
    fo.write("NO")