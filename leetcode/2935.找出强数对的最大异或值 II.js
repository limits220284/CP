var maximumStrongPairXor = function(nums) {
    nums=[...new Set(nums)];
    nums.sort((a,b)=>a-b);
    let res=0, n=nums.length;
    for(let i=0;i<n-1;i++){
        for(let j=i+1;j<n&&nums[j]<=nums[i]*2;j++)
            res=Math.max(res,nums[i]^nums[j]);
    }
    return res;
};
