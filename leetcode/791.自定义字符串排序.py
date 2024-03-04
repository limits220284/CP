class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        ans = []

        # Write all characters that occur in S, in the order of S.
        for c in order:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0
        
        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])
        return "".join(ans)




