class Solution:
    def twoOutOfThree(self, a: List[int], b: List[int], c: List[int]) -> List[int]:
        return list((set(a) & set(b)) | (set(b) & set(c)) | (set(a) & set(c)))