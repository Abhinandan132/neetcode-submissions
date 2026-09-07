class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // Naive approach, not doing it in place, create a separate vector, push non vals. 
        // T.C O(n), S.C: O(n); 
        // vector<int> temp;
        // for(int i = 0; i < nums.size(); i++){
        //     if (nums[i] != val)
        //         temp.push_back(nums[i]); 
        // }
        // nums = temp; 
        // return temp.size(); 
        int j = 0; 
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] != val)
                nums[j++] = nums[i]; 
        }
        return j; 
    }
};