/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const counter = {};
    for(let num of nums){
        if(num in counter){
            counter[num] += 1;
        } else {
            counter[num] = 1;
        }
        if(counter[num] > Math.floor(nums.length / 2)){
            return num;
        }
    }
};