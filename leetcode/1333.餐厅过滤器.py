class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        for restaurant in restaurants:
            if veganFriendly == 1 and restaurant[2] == 1 or veganFriendly == 0:
                if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                    ans.append(restaurant)
        ans.sort(key = lambda x: (-x[1], -x[0]))
        return [x[0] for x in ans]