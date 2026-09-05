class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Implementation of the naive solution T.C: O(n^2), S.C: O(1)
        // for(int i = 0; i < nums.size(); i++){
        //     for(int j = i + 1; j < nums.size(); j++)
        //         if ((nums[i] + nums[j]) == target)return {i, j}; 
        // }
        // return {-1, -1}; 
        int n = nums.size(); 
        unordered_map<int, int> numMap; 
        for(int i = 0; i < n; i++)
            numMap[nums[i]] = i; 
        for(int i = 0; i < n; i++){
            if (numMap.find(target - nums[i]) != numMap.end() && i != numMap[target - nums[i]]) 
                return {i, numMap[target - nums[i]]}; 
        }
        return {-1, -1}; 
    }
};
