class Heap:

    def __init__(self, nums1, nums2):
        self.arr = []
        self.nums1 = nums1
        self.nums2 = nums2

    def upheapify(self, idx):
        while(idx > 0):
            pi = int((idx-1)/int(2))
            if self.nums1[self.arr[idx].first] + self.nums2[self.arr[idx].second]  < self.nums1[self.arr[pi].first] + self.nums2[self.arr[pi].second]:
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

            if lc < len(self.arr) and self.nums1[self.arr[lc].first] + self.nums2[self.arr[lc].second] < self.nums1[self.arr[cand].first] + self.nums2[self.arr[cand].second]:
                cand = lc 

            if rc < len(self.arr) and self.nums1[self.arr[rc].first] + self.nums2[self.arr[rc].second] < self.nums1[self.arr[cand].first] + self.nums2[self.arr[cand].second]:
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
    def __init__(self, first, second):
        self.first = first 
        self.second = second 
    


mat = [[1,10,10],
        [1,4,5],
        [2,3,6]]
k = 7
n = len(mat)
m = len(mat[0])



def kSmallestPairs(nums1,nums2):
    heap = Heap(nums1, nums2)

    for i in range(len(nums1)):
        heap.insert(Node(i, 0))

    ans = []

    for i in range(k):
        if len(heap.arr) > 0:
            first = heap.arr[0].first
            second = heap.arr[0].second
            ans.append(nums1[first] + nums2[second])
            heap.remove()
            second += 1

            if second < len(nums2):
                heap.insert(Node(first, second))

    return ans
row = mat[0]
for i in range(1, n):
    row = kSmallestPairs(row, mat[i])

print(row[k-1])






