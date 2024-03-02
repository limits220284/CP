class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = Counter(positive_feedback)
        negative_feedback = Counter(negative_feedback)
        n = len(student_id)
        ans = []
        for i in range(n):
            t = 0
            for ss in report[i].split():
                if ss in positive_feedback:
                    t += 3
                elif ss in negative_feedback:
                    t -= 1
            ans.append([-t, student_id[i]])
        ans.sort()
        return [i for v, i in ans[:k]]
                
