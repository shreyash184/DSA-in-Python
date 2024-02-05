class Heap:

    def __init__(self, arr):
        self.arr = arr 
        self.build_heap()

    def build_heap(self):
        for i in reversed(range(len(self.arr))):
            self.downheapify(i)

    def upheapify(self, idx):
        while(idx > 0):
            pi = int((idx-1)/int(2))
            if self.arr[idx] > self.arr[pi]:
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

            if lc < len(self.arr) and self.arr[lc] > self.arr[cand]:
                cand = lc 

            if rc < len(self.arr) and self.arr[rc] > self.arr[cand]:
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


arr = [9,5,1,2,3,0,11,6]
heap = Heap(arr)
heap.display()
# 3,2,3,1,2,4,5,5,6



