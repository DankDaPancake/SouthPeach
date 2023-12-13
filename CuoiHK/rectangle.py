fi = open('rectangle.inp', 'r')
fo = open('rectangle.out', 'w')

m, n = map(int, fi.readline().split())
b = []
for i in range(m):
    b.append(list(fi.readline().split()))
#print(b)

def maxRec(H): 
    stack = []
    maxA = 0
    m = len(H)

    for i in range(m+1):
        while stack and (i == m or H[stack[-1]] >= H[i]):
            height = H[stack.pop()]
            width = 0
            if not stack: width = i
            else: width = i - stack[-1] - 1
            maxA = max(maxA, height * width)
        stack.append(i)

    return maxA

def maxSum():
    ans = 0
    h = [0] * n

    for i in range(m):
        for j in range(n):
            if b[i][j] == '1': h[j] += 1
            else: h[j] = 0
        area = maxRec(h)
        ans = max(ans, area)

    return ans

if not b: fo.write('0')
fo.write(str(maxSum()))