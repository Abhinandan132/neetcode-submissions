class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size(); 
        unordered_map<int, int> sumHash;  
        for(int i = 0; i < n; i++){
            int n1 = nums[i]; 
            if (sumHash.find(target - n1) != sumHash.end()){
                return i < sumHash[target -n1]?vector<int>{i, sumHash[target - n1]}:vector<int>{sumHash[target - n1], i}; 
            }
            // Record index. 
            sumHash[n1] = i; 
        }
        return {-1, -1};
    }
};
