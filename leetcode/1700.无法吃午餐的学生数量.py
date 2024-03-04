class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # hash表做法
        dic=Counter(students)
        print(dic)
        i,n=0,len(sandwiches)
        while i<n:
            if dic[sandwiches[i]]:
                dic[sandwiches[i]]-=1
            else:break
            i+=1
        return n-i