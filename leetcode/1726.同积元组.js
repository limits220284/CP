/**
 * @param {number[]} nums
 * @return {number}
 */
var tupleSameProduct = function(nums) {
    const n = nums.length;
    const cnt = new Map();
    for(let i = 0; i < n; i++){
        for(let j = i + 1; j < n; j++){
            const key = nums[i] * nums[j];
            cnt.set(key, (cnt.get(key) || 0) + 1);
        }
    }
    let ans = 0;
    for(const v of cnt.values()){
        ans += v * (v - 1) * 4;
    }
    return ans;
};