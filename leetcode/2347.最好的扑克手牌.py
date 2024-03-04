class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        mx = 0
        for (x,y) in Counter(ranks).items():
            mx = max(mx,y)
        if mx >= 3:
            return "Three of a Kind"
        if mx ==2:
            return "Pair"
        return "High Card"