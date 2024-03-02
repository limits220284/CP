class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        print(courses)
        tot = 0
        h = []
        for d, l in courses:
            tot += d
            heappush(h, -d)
            while tot > l:
                tot += heappop(h)
        return len(h)