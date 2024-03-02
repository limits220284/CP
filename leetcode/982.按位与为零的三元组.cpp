#include<immintrin.h>

__attribute__((no_sanitize_address,no_sanitize_memory))
__attribute__((target("avx2")))
void fwt(int* seq, int n) {
    const auto end = seq + n;
    for (int i = 1;i < 8 && i < n;i *= 2)
        for (auto j = seq;j != end;j += i)
            for (const auto k = j + i;j < k;++j)
                *j += j[i];
    const int m = n / 8;
    const auto l = reinterpret_cast<__m256i*>(seq);
    const auto r = reinterpret_cast<__m256i*>(end);
    for (int i = 1;i < m;i *= 2)
        for (auto j = l;j != r;j += i)
            for (const auto k = j + i;j < k;++j)
                *j = _mm256_add_epi32(*j, j[i]);
}

class Solution {
public:
    int countTriplets(const vector<int>& nums) {
        const int m = *max_element(nums.begin(), nums.end());
        const int l = m > 0 ? 1 << (32 - __builtin_clz(m)) : 1;
        alignas(32) int seq[l];
        fill_n(seq, l, 0);
        for (int e : nums)
            ++seq[e];
        fwt(seq, l);
        int ans = 0;
        for (int i = 0;i <= m;++i)
            ans += (1 - 2 * __builtin_parity(i)) * seq[i] * seq[i] * seq[i];
        return ans;
    }
};