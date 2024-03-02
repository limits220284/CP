class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # 贪心，找到和其他人存在沟通障碍的人
        person = defaultdict(set)
        for i, arr in enumerate(languages):
            person[i+1] = set(arr)
        no = set()
        for x, y in friendships:
            if not (person[x] & person[y]):
                no.add(x);no.add(y)
        if len(no) == 0: return 0
        cnt = Counter()
        for r in no:
            for x in languages[r-1]:
                cnt[x] += 1
        return len(no) - max(cnt.values())
            
