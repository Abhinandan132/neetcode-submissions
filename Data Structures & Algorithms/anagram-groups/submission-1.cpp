class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Store sorted hash values, with vectors of words that become k, when v is sorted. // Naive approach T.C O(n * m log m) S.C O(m * n)
        // unordered_map<string, vector<string>> mpp; 
        // vector<vector<string>> ans; 
        // for(int i = 0; i < strs.size(); i++){
        //     string tmp = strs[i]; 
        //     sort(tmp.begin(), tmp.end()); 
        //     mpp[tmp].push_back(strs[i]); 
        // }
        // for(auto &it: mpp)ans.push_back(it.second); 
        // return ans; 

    // Hashing with frequency arrays. 
        unordered_map<string, vector<string>> mpp; 
        vector<vector<string>> ans; 
        for(const auto &s: strs){
            vector<int> count(26, 0); 
            for(auto &c: s)
                count[c - 'a']++; 
            string key = to_string(count[0]); 
            for(int i = 1; i < 26; i++)key += ',' + to_string(count[i]); 
            mpp[key].push_back(s); 
        }
        for(const auto &pair: mpp)ans.push_back(pair.second); 
        return ans; 
    }
};
