class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Is nums sorted? 
        int n = nums.size(); 
        unordered_map<int, int> freqMap; 
        for(int i = 0; i < n; i++)
            freqMap[nums[i]]++; 
        for(int num: nums){
            if (freqMap[num] > 1)
                return true; 
        } 
        return false; 
    }
};