/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    strs.sort();
    first = strs[0];
    last = strs[strs.length - 1];
    ans = "";
    for(let i=0; i<Math.min(first.length, last.length); i++){
        if(first[i] == last[i]){
            ans += first[i];
        } else {
            return ans;
        }
    }
    return null;
};