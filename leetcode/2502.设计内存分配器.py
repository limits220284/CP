class Allocator:

    def __init__(self, n: int):
        self.arr=[0]*n
        self.n=n
        
    def allocate(self, size: int, mID: int) -> int:
        i=0
        while i<self.n:
            if self.arr[i]==0:
                k=0
                while i+k<self.n and self.arr[i+k]==0:
                    k+=1
                if k>=size:
                    for j in range(size):
                        self.arr[i+j]=mID
                    return i
                else:
                    i+=k
            else:
                i+=1
        return -1
            
    def free(self, mID: int) -> int:
        cnt=0
        for i in range(self.n):
            if self.arr[i]==mID:
                self.arr[i]=0
                cnt+=1
        return cnt



# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)