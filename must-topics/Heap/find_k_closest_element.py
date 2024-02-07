class Heap:

    def __init__(self):
        self.arr = []

    def upheapify(self, idx):
        while(idx > 0):
            pi = int((idx-1)/int(2))
            if self.arr[idx].act_val >= self.arr[pi].act_val:
                self.arr[idx], self.arr[pi] = self.arr[pi], self.arr[idx]
                idx = pi
            else:
                break
        
    def insert(self, data):
        self.arr.append(data)
        self.upheapify(len(self.arr) - 1)
    
    def downheapify(self, idx):
        while idx < len(self.arr):
            lc = 2 * idx + 1
            rc = 2 * idx + 2
            cand = idx 

            if lc < len(self.arr) and self.arr[lc].act_val > self.arr[cand].act_val:
                cand = lc 

            if rc < len(self.arr) and self.arr[rc].act_val > self.arr[cand].act_val:
                cand = rc 

            if cand == idx: 
                break

            self.arr[cand], self.arr[idx] = self.arr[idx], self.arr[cand]
            idx = cand 

    # This only remove the root element, We can also make for any element
    def remove(self):
        self.arr[0], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[0]
        self.arr.pop()
        self.downheapify(0)

    def get(self):
        if len(self.arr) > 0:
            return self.arr[0]
        return -1 * 2 ** 31 - 1


class Node:
    def __init__(self, val, x):
        self.val = val
        self.act_val = abs(self.val - x)
    
heap = Heap()

arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
ans = []
for i in range(k):
    heap.insert(Node(arr[i], x))

print(len(heap.arr))

for i in range(k, len(arr)):
    heap.insert(Node(arr[i], x))
    heap.remove()

for i in range(len(heap.arr)):
    ans.append(heap.arr[i].val)

ans.sort()
print(ans)

# I think this can be done in a better way


