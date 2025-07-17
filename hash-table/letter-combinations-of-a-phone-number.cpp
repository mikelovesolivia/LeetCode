class Solution {
public:
    void backtrack(int idx, string comb, vector<string>& result, string digits, unordered_map<char, string> nums){
            if(idx == digits.size()){
                result.push_back(comb);
                return;
            }
            for(auto letter: nums[digits[idx]]){
                backtrack(idx + 1, comb + letter, result, digits, nums);
            }
        }
    vector<string> letterCombinations(string digits) {
        if(digits.empty()){
            return {};
        }
        unordered_map<char, string> nums = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        
        vector<string> result;
        backtrack(0, "", result, digits, nums);
        return result;
    }
};