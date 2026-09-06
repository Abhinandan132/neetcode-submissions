class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Store sorted hash values, with vectors of words that become k, when v is sorted. 
        unordered_map<string, vector<string>> mpp; 
        vector<vector<string>> ans; 
        for(int i = 0; i < strs.size(); i++){
            string tmp = strs[i]; 
            sort(tmp.begin(), tmp.end()); 
            mpp[tmp].push_back(strs[i]); 
        }
        for(auto &it: mpp)ans.push_back(it.second); 
        return ans; 
    }
};
