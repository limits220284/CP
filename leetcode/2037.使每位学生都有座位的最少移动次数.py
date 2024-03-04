class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 1 3 5
        # 3 4 7
        # 假设a,b 为位置
        # x,y为学生
        # x=b 此时移动次数为y-a
        # x-a+y-b=x-b+y-a=y-a
        return sum(abs(x-y) for x,y in zip(sorted(seats),sorted(students)))
