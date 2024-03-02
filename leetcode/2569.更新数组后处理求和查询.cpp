#include <immintrin.h>
class Solution {
public:
    __attribute__((target("avx512vpopcntdq"))) vector<long long> handleQuery(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        static uint8_t data[(100000 + 511) / 512 * 512] __attribute__((aligned(512)));
        int n = nums1.size();

        int *pIn = nums1.data(), *pInEnd64 = pIn + n / 64 * 64, *pInEnd = pIn + n;
        uint64_t *pOut = (uint64_t*)data, *pOutEnd = pOut + (n + 511) / 512 * (512 / 64);
        while (pIn < pInEnd64) {
            uint64_t x = 0;
            for (int i = 0; i < 64; i++) x |= (uint64_t)*pIn++ << i;
            *pOut++ = x;
        }
        {
            uint64_t x = 0;
            int i = 0;
            while (pIn < pInEnd) x |= (uint64_t)*pIn++ << i++;
            *pOut++ = x;
        }
        while (pOut < pOutEnd) *pOut++ = 0;

        long long s = 0;
        for (int x : nums2) s += x;
        vector<long long> res;

        uint8_t *dataEnd = (uint8_t*)pOutEnd;
        uint64_t ones64 = -1;
        __m512i ones512 = _mm512_set1_epi32(-1);
        for (auto& query : queries) {
            int op = query[0], l = query[1], r = query[2] + 1;
            switch (op) {
                case 1: {
                    int l64 = (l + 63) / 64 * 64, l512 = (l + 511) / 512 * 512;
                    uint8_t *pl64 = data + l64 / 8, *pl512 = data + l512 / 8;
                    int r64 = r / 64 * 64, r512 = r / 512 * 512;
                    uint8_t *pr64 = data + r64 / 8, *pr512 = data + r512 / 8;
                    if (r64 < l64) {
                        *(uint64_t*)pr64 ^= (ones64 << (l - r64)) & (ones64 >> (l64 - r));
                        break;
                    }
                    if (l < l64) {
                        *(uint64_t*)(pl64 - 8) ^= ones64 << (64 - (l64 - l));
                    }
                    if (r512 < l512) {
                        for (uint64_t *p = (uint64_t*)pl64; p < (uint64_t*)pr64; p++) *p ^= ones64;
                    } else {
                        for (uint64_t *p = (uint64_t*)pl64; p < (uint64_t*)pl512; p++) *p ^= ones64;
                        for (__m512i *p = (__m512i*)pl512; p < (__m512i*)pr512; p++) {
                            *p = _mm512_xor_epi32(*p, ones512);
                        }
                        for (uint64_t *p = (uint64_t*)pr512; p < (uint64_t*)pr64; p++) *p ^= ones64;
                    }
                    if (r64 < r) {
                        *(uint64_t*)pr64 ^= ones64 >> (64 - (r - r64));
                    }
                    break;
                }
                case 2: {
                    __m512i accumulator = _mm512_setzero_si512();
                    for (__m512i *p = (__m512i*)data; p < (__m512i*)dataEnd; p++) {
                        accumulator = _mm512_add_epi64(accumulator, _mm512_popcnt_epi64(*p));
                    }
                    uint64_t total = 0;
                    for (int i = 0; i < 8; i++) total += accumulator[i];
                    s += total * l;
                    break;
                }
                default:
                    res.push_back(s);
            }
        }
        return res;
    }
};
int __FAST_IO__ = []() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    return 0;
}();
 