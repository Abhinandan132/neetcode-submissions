class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> counter; 
        for(int i = 0; i < nums.size(); i++){
            counter[nums[i]]++; 
            if (counter[nums[i]] > 1)return true; 
        }
        return false; 
    }
};