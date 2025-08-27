/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    const dp = Array(nums.length).fill(0);
    dp[0] = nums[0];
    for(let i=1;i<nums.length;i++){
        dp[i] = Math.max(dp[i-1], i+nums[i]);
    }
    for(let i=0;i<nums.length;i++){
        if(dp[i] == i) return false;
        if(dp[i] >= nums.length-1) return true;
    }
};