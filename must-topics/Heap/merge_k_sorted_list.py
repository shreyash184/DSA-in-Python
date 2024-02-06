# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = Heap()
        head = ListNode(0)
        point = head

        for ll in lists:
            if ll:
                heap.insert(ll)
        
        while len(heap.arr) > 0:
            node = heap.arr[0]
            heap.remove()
            point.next = ListNode(node.val)
            point = point.next
            node = node.next

            if node:
                heap.insert(node)

        return head.next