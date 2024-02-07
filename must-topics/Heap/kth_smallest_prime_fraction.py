arr = list()
class Heap:

    def __init__(self, lst):
        self.arr = []
        self.lst = lst

    def upheapify(self, idx):
        while(idx > 0):
            pi = int((idx-1)/int(2))
            if (self.lst[self.arr[idx].nominator] / self.lst[self.arr[idx].denominator]) < (self.lst[self.arr[pi].nominator] / self.lst[self.arr[pi].denominator]):
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

            if lc < len(self.arr) and (self.lst[self.arr[lc].nominator] / self.lst[self.arr[lc].denominator]) < (self.lst[self.arr[cand].nominator] / self.lst[self.arr[cand].denominator]):
                cand = lc 

            if rc < len(self.arr) and (self.lst[self.arr[rc].nominator] / self.lst[self.arr[rc].denominator]) < (self.lst[self.arr[cand].nominator] / self.lst[self.arr[cand].denominator]):
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

class Node():
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = Heap(arr)
        last_element = len(arr) - 1

        for i in range(len(arr)):
            heap.insert(Node(i, last_element))

        for i in range(k-1):
            nominator = heap.arr[0].nominator
            denominator = heap.arr[0].denominator
            denominator -= 1

            heap.remove()
            if nominator < denominator:
                heap.insert(Node(nominator, denominator))

        return [arr[heap.arr[0].nominator], arr[heap.arr[0].denominator]]