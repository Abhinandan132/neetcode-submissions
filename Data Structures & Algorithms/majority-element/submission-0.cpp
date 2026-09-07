class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Naive approach is to use hashing. 
        unordered_map<int, int> mpp; 
        for(int i = 0; i < nums.size(); i++)mpp[nums[i]]++; 
        for(const auto &pair: mpp){
            if (pair.second > nums.size()/2)return pair.first; 
        }
        return -1; // Place holder. 
    }
};