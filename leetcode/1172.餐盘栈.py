"""
分析:
1、push操作: 需要快速的找到第一个没有满的栈，这个栈具有一个性质就是下标最小
2、pop操作：返回从左往右的第一个非空栈顶部的值，将其从栈中删除
3、直接返回编号为index的栈顶部的值
- 需要一个logn时间复杂度能够扩容的数据结构，如果某个栈为空了直接删除即可
- 能够快速找到第一个不满的栈，可能第一个是满的，但是第二个是不满的，这个时候需要删除第二个，而不是第一个

- 算法:
    - 初始化堆和stacks
    - 
"""
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stks = []
        self.h = []
        self.capacity = capacity
    def push(self, val: int) -> None:
        # 如果栈不为空，而且栈顶的元素值都大于当前栈的最长长度，直接清空栈即可
        if len(self.h) and self.h[0] >= len(self.stks):
            self.h = []
        # 如果最小堆为空，新建一个栈，然后将栈的下标入堆
        n = len(self.stks)
        if len(self.h) == 0: # 表示没有不满的栈了
            stk = [val]
            if self.capacity > 1:
                heappush(self.h, n)
            self.stks.append(deepcopy(stk))
        else:
            t = self.h[0]
            self.stks[t].append(val)
            # 如果加入当前元素，栈的容量满了之后，就直接pop掉该满栈
            if len(self.stks[t]) == self.capacity:
                heappop(self.h)
    def pop(self) -> int:
        # 直接返回最后一个栈的值，如果当前栈为空了，直接pop掉即可
        return self.popAtStack(len(self.stks) - 1)

    def popAtStack(self, index: int) -> int:
        # 直接返回栈顶部的值
        # 如果操作的是一个满栈，那么将下标存进堆里
        # 如果当前栈元素只有一个值，pop就pop了，不用管，只有最后一个栈需要管
        if index < 0 or index >= len(self.stks) or len(self.stks[index]) == 0:
            return -1
        # if len(self.stks[index]) == self.capacity:
        #     heappush(self.h, index)
        # val = self.stks[index].pop()
        # while self.stks and len(self.stks[-1]) == 0:
        #     self.stks.pop()
        # return val
        if index != len(self.stks) - 1:
            if len(self.stks[index]) == 0:
                return -1
            else:
                if len(self.stks[index]) == self.capacity:
                    heappush(self.h, index)
                ans = self.stks[index].pop()
                while self.stks and len(self.stks[-1]) == 0:
                    self.stks.pop()
                return ans
        else:
            if len(self.stks[index]) != 0:
                if len(self.stks[index]) == self.capacity:
                    heappush(self.h, index)
                ans = self.stks[index].pop()
                while self.stks and len(self.stks[-1]) == 0:
                    self.stks.pop()
                return ans
            else:
                while self.stks and len(self.stks[-1]) == 0:
                    self.stks.pop()
                return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)