class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Naive approach is to use hashing. 
        // unordered_map<int, int> mpp; 
        // for(int i = 0; i < nums.size(); i++)mpp[nums[i]]++; 
        // for(const auto &pair: mpp){
        //     if (pair.second > nums.size()/2)return pair.first; 
        // }
        // return -1; // Place holder.
        int e = 0, cnt = 0; 
        for(int i = 0; i < nums.size(); i++){
            if (cnt == 0)e = nums[i]; 
            cnt += (nums[i] == e)? 1: -1; 
        }
        return e; 
    }
};