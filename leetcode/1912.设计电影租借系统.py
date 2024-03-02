from sortedcontainers import SortedList
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.n = n
        self.Have = defaultdict(SortedList)
        self.DonotHave = SortedList()
        self.entries = defaultdict(defaultdict)
        for s, m, p in entries:
            self.Have[m].add((p, s))
            self.entries[s][m] = p
    def search(self, movie: int) -> List[int]:
        arr = self.Have[movie]
        ans = []
        for i in range(min(5, len(arr))):
            ans.append(arr[i][1])
        return ans
    def rent(self, shop: int, movie: int) -> None:
        self.Have[movie].remove((self.entries[shop][movie], shop))
        self.DonotHave.add((self.entries[shop][movie], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.DonotHave.remove((self.entries[shop][movie], shop, movie))
        self.Have[movie].add((self.entries[shop][movie], shop))
    def report(self) -> List[List[int]]:
        ans = []
        for i in range(min(5, len(self.DonotHave))):
            ans.append([self.DonotHave[i][1], self.DonotHave[i][2]])
        return ans



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()