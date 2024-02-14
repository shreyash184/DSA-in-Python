






n = int(input())
m = int(input())

boxes = [0] * (n)

while m > 0:
    l, r = list(map(int, input().split()))
    boxes[l-1] += 1
    if (r < n):
        boxes[r] -= 1
    m -= 1

for i in range(1, n):
    boxes[i] += boxes[i-1]

# print(boxes)

q = int(input())
freq = [0] * (1000001)

for box in boxes:
    freq[box] += 1

for i in reversed(range(0, 1000000)):
    freq[i] += freq[i+1]

# print(freq)
while q > 0:
    x = int(input())
    print(freq[x])
    q -= 1
