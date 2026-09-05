class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Implementation of the naive solution T.C: O(n^2), S.C: O(1)
        // for(int i = 0; i < nums.size(); i++){
        //     for(int j = i + 1; j < nums.size(); j++)
        //         if ((nums[i] + nums[j]) == target)return {i, j}; 
        // }
        // return {-1, -1}; 
        unordered_map<int, int> numMap; 
        for(int i = 0; i < nums.size(); i++){
            int y = target - nums[i]; 
            if (numMap.find(y) != numMap.end())return {numMap[y], i}; 
            numMap[nums[i]] = i; 
        }
        return {}; 
    }
};
