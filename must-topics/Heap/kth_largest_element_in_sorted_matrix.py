class Heap:

    def __init__(self):
        self.arr = []

    def upheapify(self, idx):
        while(idx > 0):
            pi = int((idx-1)/int(2))
            if self.arr[idx].val < self.arr[pi].val:
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

            if lc < len(self.arr) and self.arr[lc].val < self.arr[cand].val:
                cand = lc 

            if rc < len(self.arr) and self.arr[rc].val < self.arr[cand].val:
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
    
    def display(self):
        print(self.arr, sep=" ")

class Node:
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col 
        
    
heap = Heap()
arr = [[1,5,9], [10,11,13], [12,13,15]]
k = 2

for r in range(min(len(arr), k)):
    heap.insert(Node(arr[r][0], r, 0))

while k-1 > 0:
    element = heap.arr[0]
    heap.remove()
    row = element.row
    col = element.col 

    if col < len(arr)-1:
        heap.insert(Node(arr[row][col+1], row, col+1))
    k = k - 1

print(heap.arr[0].val)




